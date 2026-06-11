import pandas as pd
import plotly.express as px
from dash import html, dcc, Input, Output
from pathlib import Path
import ast
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from src.analysis.metrics import calculo_radio, calculo_densidad_lex


def cargar_df():
    base = Path(__file__).resolve().parent.parent.parent
    ruta = base / 'data' / 'processed' / 'resenas_pos_tagged.csv'
    df = pd.read_csv(ruta)
    df['tokens_spacy'] = df['tokens_spacy'].apply(ast.literal_eval)
    df['polaridad'] = df['calificación'].apply(
        lambda x: 'positiva' if x >= 4 else ('negativa' if x <= 2 else 'neutral'))
    return df


df = cargar_df()


def layout():
    return html.Div([
        html.H2("⚖️ Comparación por Polaridad", style={'textAlign': 'center'}),
        dcc.Graph(id='polaridad-metricas'),
        dcc.Graph(id='polaridad-distribucion')
    ])


def register_callbacks(app):
    @app.callback(
        Output('polaridad-metricas', 'figure'),
        Output('polaridad-distribucion', 'figure'),
        Input('polaridad-metricas', 'id')  # dummy
    )
    def update_polaridad(_):
        # Calcular métricas por polaridad
        metricas = []
        for pol in ['positiva', 'negativa', 'neutral']:
            sub = df[df['polaridad'] == pol]
            if len(sub) == 0:
                continue
            sub['radio'] = sub['tokens_spacy'].apply(calculo_radio)
            sub['densidad'] = sub['tokens_spacy'].apply(calculo_densidad_lex)
            metricas.append({
                'Polaridad': pol,
                'Ratio N/V': sub['radio'].mean(),
                'Densidad Léxica': sub['densidad'].mean()
            })
        df_met = pd.DataFrame(metricas)

        fig1 = px.bar(df_met, x='Polaridad', y=['Ratio N/V', 'Densidad Léxica'],
                      barmode='group', title='Comparación de métricas por polaridad',
                      color_discrete_sequence=['#2E86AB', '#A2D4AB'])
        fig1.update_layout(template='plotly_white')

        # Distribución POS para cada polaridad (top 5)
        # Usamos la función distribucion_pos (necesitas importarla)
        from src.analysis.pos_analyzer import distribucion_pos
        dfs_pos = {}
        for pol in ['positiva', 'negativa']:
            sub = df[df['polaridad'] == pol]
            if len(sub) > 0:
                dfs_pos[pol] = distribucion_pos(sub['tokens_spacy']).head(5)
                dfs_pos[pol]['Polaridad'] = pol

        if dfs_pos:
            df_plot = pd.concat(dfs_pos.values())
            fig2 = px.bar(df_plot, x='Categoría', y='Porcentaje', color='Polaridad',
                          barmode='group', title='Distribución POS (top 5) por polaridad',
                          text_auto='.1f')
            fig2.update_layout(template='plotly_white')
        else:
            fig2 = px.bar(title="No hay suficientes datos")
        return fig1, fig2
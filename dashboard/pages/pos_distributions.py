import pandas as pd
import plotly.express as px
from dash import html, dcc, Input, Output
from pathlib import Path
import ast
from collections import Counter
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from src.analysis.pos_analyzer import distribucion_pos


# Cargar datos
def cargar_df():
    base = Path(__file__).resolve().parent.parent.parent
    ruta = base / 'data' / 'processed' / 'resenas_pos_tagged.csv'
    df = pd.read_csv(ruta)
    df['tokens_spacy'] = df['tokens_spacy'].apply(ast.literal_eval)
    df['polaridad'] = df['calificación'].apply(
        lambda x: 'positiva' if x >= 4 else ('negativa' if x <= 2 else 'neutral')
    )
    return df


df = cargar_df()


# Layout de la página
def layout():
    return html.Div([
        html.H2("📊 Distribución de Categorías Gramaticales (POS)",
                style={'textAlign': 'center', 'color': '#2E86AB'}),
        html.Div([
            html.Div([
                html.Label("Filtrar por tipo de lugar:"),
                dcc.Dropdown(
                    id='pos-tipo',
                    options=[{'label': 'Todos', 'value': 'todos'}] +
                            [{'label': t.capitalize(), 'value': t} for t in df['tipo_lugar'].unique()],
                    value='todos',
                    clearable=False
                )
            ], style={'width': '30%', 'display': 'inline-block', 'padding': '10px'}),
            html.Div([
                html.Label("Filtrar por polaridad:"),
                dcc.Dropdown(
                    id='pos-polaridad',
                    options=[{'label': 'Todas', 'value': 'todas'}] +
                            [{'label': p.capitalize(), 'value': p} for p in df['polaridad'].unique()],
                    value='todas',
                    clearable=False
                )
            ], style={'width': '30%', 'display': 'inline-block', 'padding': '10px'})
        ], style={'display': 'flex', 'justifyContent': 'center'}),
        dcc.Graph(id='pos-grafico'),
        html.Div(id='pos-stats', style={'textAlign': 'center', 'marginTop': '20px'})
    ])


def register_callbacks(app):
    @app.callback(
        Output('pos-grafico', 'figure'),
        Output('pos-stats', 'children'),
        Input('pos-tipo', 'value'),
        Input('pos-polaridad', 'value')
    )
    def update_pos(tipo, polaridad):
        df_filt = df.copy()
        if tipo != 'todos':
            df_filt = df_filt[df_filt['tipo_lugar'] == tipo]
        if polaridad != 'todas':
            df_filt = df_filt[df_filt['polaridad'] == polaridad]

        if df_filt.empty:
            return px.bar(title="No hay datos con estos filtros"), "No hay datos"

        # Reutilizamos la función distribucion_pos (devuelve DataFrame con Categoría y Porcentaje)
        df_pos = distribucion_pos(df_filt['tokens_spacy'])
        # Mostramos top 10
        df_top = df_pos.head(10)

        fig = px.bar(df_top, x='Categoría', y='Porcentaje',
                     title=f'Distribución POS - {tipo if tipo != "todos" else "Todos"} / {polaridad if polaridad != "todas" else "Todas"}',
                     text_auto='.1f', color_discrete_sequence=['#2E86AB'])
        fig.update_layout(template='plotly_white', xaxis_title='Categoría POS', yaxis_title='Porcentaje (%)')
        fig.update_traces(marker_line_color='black', marker_line_width=1)

        total_resenas = len(df_filt)
        stats = f"📌 Reseñas consideradas: {total_resenas} | Total de etiquetas analizadas: {df_pos['Frecuencia'].sum()}"
        return fig, stats
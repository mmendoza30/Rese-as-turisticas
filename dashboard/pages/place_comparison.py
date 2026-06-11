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
    return df


df = cargar_df()


def layout():
    return html.Div([
        html.H2("📍 Comparación por Tipo de Lugar", style={'textAlign': 'center'}),
        dcc.Graph(id='place-radio'),
        dcc.Graph(id='place-densidad')
    ])


def register_callbacks(app):
    @app.callback(
        Output('place-radio', 'figure'),
        Output('place-densidad', 'figure'),
        Input('place-radio', 'id')
    )
    def update_place(_):
        # Calcular métricas por tipo de lugar
        tipos = df['tipo_lugar'].unique()
        radios = []
        densidades = []
        for t in tipos:
            sub = df[df['tipo_lugar'] == t]
            sub_radio = sub['tokens_spacy'].apply(calculo_radio).mean()
            sub_dens = sub['tokens_spacy'].apply(calculo_densidad_lex).mean()
            radios.append({'tipo': t, 'Ratio N/V': sub_radio})
            densidades.append({'tipo': t, 'Densidad Léxica': sub_dens})

        df_radio = pd.DataFrame(radios)
        df_dens = pd.DataFrame(densidades)

        fig1 = px.bar(df_radio, x='tipo', y='Ratio N/V', title='Ratio Sustantivos/Verbos por tipo de lugar',
                      color_discrete_sequence=['#FFB347'])
        fig1.update_layout(template='plotly_white', xaxis_title='Tipo de lugar', yaxis_title='Ratio N/V')

        fig2 = px.bar(df_dens, x='tipo', y='Densidad Léxica', title='Densidad Léxica por tipo de lugar',
                      color_discrete_sequence=['#6A9FB5'])
        fig2.update_layout(template='plotly_white', xaxis_title='Tipo de lugar',
                           yaxis_title='Densidad Léxica (proporción)')

        return fig1, fig2
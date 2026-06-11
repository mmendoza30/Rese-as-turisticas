from dash import Dash, dcc, html, Input, Output
from pages import pos_distributions, polarity_comparison, place_comparison, home

app = Dash(__name__, suppress_callback_exceptions=True)
app.title = "Análisis POS - Reseñas Turísticas Costa Rica"

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        html.H1("📊 Análisis Morfosintáctico de Reseñas Turísticas de Costa Rica",
                style={'textAlign': 'center', 'color': '#1e3c72', 'marginBottom': '5px'}),
        html.Hr(),
        html.Div([
            dcc.Link('🏠 Inicio', href='/', className='nav-link'),
            html.Span(' | '),
            dcc.Link('📊 Distribución POS', href='/pos', className='nav-link'),
            html.Span(' | '),
            dcc.Link('⚖️ Comparación por Polaridad', href='/polarity', className='nav-link'),
            html.Span(' | '),
            dcc.Link('📍 Comparación por Tipo de Lugar', href='/place', className='nav-link'),
        ], style={'textAlign': 'center', 'padding': '10px', 'backgroundColor': '#f0f2f5'})
    ]),
    html.Div(id='page-content', style={'padding': '20px'})
])

# Registrar callbacks de cada página
pos_distributions.register_callbacks(app)
polarity_comparison.register_callbacks(app)
place_comparison.register_callbacks(app)

@app.callback(Output('page-content', 'children'), Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/pos':
        return pos_distributions.layout()
    elif pathname == '/polarity':
        return polarity_comparison.layout()
    elif pathname == '/place':
        return place_comparison.layout()
    else:
        return home.layout()

if __name__ == '__main__':
    app.run(debug=True)
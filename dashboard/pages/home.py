from dash import html

def layout():
    return html.Div([
        html.Div([
            html.H2("🌿 Análisis de Reseñas Turísticas de Costa Rica",
                    style={'textAlign': 'center', 'color': '#1E5631'}),
            html.P([
                "Este dashboard explora la estructura morfosintáctica (etiquetado POS) de reseñas turísticas de Costa Rica. ",
                "Utilizando técnicas de Procesamiento de Lenguaje Natural (PLN) con NLTK y spaCy, se identifican patrones gramaticales ",
                "que diferencian reseñas positivas de negativas, así como entre distintos tipos de lugares (hoteles, restaurantes, parques nacionales)."
            ], style={'textAlign': 'justify', 'fontSize': '1.1rem', 'marginTop': '20px', 'lineHeight': '1.6'}),
            html.P([
                "📊 **Distribución POS**: muestra las categorías gramaticales más frecuentes (sustantivos, verbos, adjetivos, etc.).",
                html.Br(),
                "⚖️ **Comparación por Polaridad**: compara métricas (ratio sustantivos/verbos, densidad de adjetivos) entre reseñas positivas y negativas.",
                html.Br(),
                "📍 **Comparación por Tipo de Lugar**: analiza diferencias gramaticales entre parques, hoteles y restaurantes."
            ], style={'marginTop': '20px', 'fontSize': '1rem'}),
            html.P("Selecciona una opción del menú para explorar los resultados.",
                   style={'fontStyle': 'italic', 'textAlign': 'center', 'marginTop': '30px'})
        ], className='card')
    ])
html.Footer("🇨🇷 Pura Vida - Costa Rica",
            style={'textAlign': 'center', 'marginTop': '40px', 'color': '#4C9A2A', 'fontWeight': '500'})
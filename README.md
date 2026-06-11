# Análisis Morfosintáctico de Reseñas Turísticas de Costa Rica aplicando POS Tagging

## 📝 Descripción del Proyecto
Este proyecto aplica técnicas avanzadas de Procesamiento de Lenguaje Natural (PLN) para analizar la estructura morfosintáctica de reseñas turísticas en español basado en diversos lugares, restaurantes y hoteles de Costa Rica. 

A través del **Part-of-Speech (POS) Tagging**, exploramos y contrastamos los patrones gramaticales que emergen según la polaridad de las opiniones (positivas vs. negativas), el tipo de lugar (parques nacionales, hoteles, restaurantes) y evaluamos cómo influye la composición lingüística en la carga emocional de los textos de las reseñas.

---

## 👥 Autores
* **Fernando Contreras**
* **Mónica Mendoza**

---

## 🎯 Objetivos de Aprendizaje
* **Objetivo General:** Aplicar técnicas de POS Tagging mediante el uso de **NLTK** y **spaCy** para descubrir patrones gramaticales en reseñas turísticas de Costa Rica, evaluando la relación entre la estructura lingüística y la carga emocional.
* **Comparación por Polaridad:** Contrastar la distribución de categorías gramaticales, densidad de adjetivos y el ratio sustantivos/verbos entre reseñas positivas (4-5 estrellas) y negativas (1-2 estrellas).
* **Análisis por Tipo de Lugar:** Identificar variaciones en el lenguaje descriptivo utilizado para clasificar y evaluar parques nacionales, hoteles y restaurantes.
* **Dominio Técnico:** Desarrollar competencias en la suite de PLN en español, contrastando sistemas de etiquetas tradicionales (**Penn Treebank**) frente a estándares modernos (**Universal POS**).

---

## 🛠️ Herramientas y Tecnologías Utilizadas
* **Lenguaje:** Python
* **Procesamiento de Lenguaje Natural (PLN):** * `spaCy` (Pipeline principal con el modelo robusto en español: `es_core_news_md`)
    * `NLTK` (Análisis comparativo de sistemas de etiquetas)
* **Análisis de Datos:** `pandas`, `Counter`
* **Visualización y Dashboard:** `Plotly Dash` y `matplotlib` *(Nota: No se utiliza Streamlit por requerimientos de arquitectura)*.

---

## 📂 Estructura del Repositorio
Para garantizar la mantenibilidad y limpieza exigidas, el código se ha organizado de forma modular de la siguiente manera:

```text
proyecto-pos-tagging-resenas/
│
├── README.md                          # Descripción del proyecto, instalación, uso
├── requirements.txt                   # Dependencias del proyecto
├── USO_DE_IA.md                       # Documentación uso de IA (OBLIGATORIO)
├── .gitignore                         # Archivos a ignorar en Git
│
├── data/                              # Datos del proyecto
│   ├── raw/                           # Datos crudos sin procesar
│   │   ├── resenas_google_maps.csv    # Reseñas reales recolectadas (Outscraper, etc.)
│   │   ├── resenas_respaldo.csv       # Dataset de respaldo en español (Kaggle)
│   │   └── metadata.json              # Metadata: lugares, fechas de recolección
│   │
│   ├── processed/                     # Datos procesados
│   │   ├── resenas_clean.csv          # Reseñas limpias
│   │   ├── resenas_tokenized.csv      # Reseñas tokenizadas
│   │   └── resenas_pos_tagged.csv     # Reseñas con POS tags
│   │
│   └── results/                       # Resultados del análisis
│       ├── pos_distributions.csv      # Distribuciones POS por polaridad/tipo de lugar
│       ├── metrics.csv                # Métricas morfosintácticas
│       └── comparisons.csv            # Comparaciones (positivas vs negativas, etc.)
│
├── notebooks/                         # Jupyter Notebooks
│   ├── 01_exploracion_datos.ipynb     # EDA del corpus de reseñas
│   ├── 02_pos_tagging_nltk.ipynb      # Implementación NLTK
│   ├── 03_pos_tagging_spacy.ipynb     # Implementación spaCy (es_core_news_md)
│   ├── 04_analisis_morfologico.ipynb  # Análisis de distribuciones y métricas
│   ├── 05_comparacion_polaridad.ipynb # Positivas (4-5★) vs negativas (1-2★)
│   ├── 06_comparacion_lugares.ipynb   # Parques vs hoteles vs restaurantes
│   └── 07_visualizaciones.ipynb       # Gráficos y dashboard
│
├── src/                               # Código fuente modular
│   ├── __init__.py                    # Inicialización del paquete
│   │
│   ├── data/                          # Módulos de manejo de datos
│   │   ├── __init__.py
│   │   ├── loader.py                  # Cargar reseñas (reales + respaldo)
│   │   ├── cleaner.py                 # Limpieza de texto (emojis, jerga)
│   │   └── preprocessor.py            # Preprocesamiento y tokenización
│   │
│   ├── pos_tagging/                   # Módulos de POS Tagging
│   │   ├── __init__.py
│   │   ├── nltk_tagger.py             # Implementación NLTK
│   │   ├── spacy_tagger.py            # Implementación spaCy
│   │   └── comparator.py              # Comparación NLTK vs spaCy
│   │
│   ├── analysis/                      # Módulos de análisis
│   │   ├── __init__.py
│   │   ├── pos_analyzer.py            # Análisis distribuciones POS
│   │   ├── metrics.py                 # Cálculo de métricas (ratio N/V, densidad léxica)
│   │   ├── polarity_comparator.py     # Comparación positivas vs negativas
│   │   └── place_comparator.py        # Comparación por tipo de lugar
│   │
│   ├── visualization/                 # Módulos de visualización
│   │   ├── __init__.py
│   │   ├── pos_plots.py               # Gráficos POS
│   │   ├── comparison_plots.py        # Gráficos comparativos
│   │   └── dashboard.py               # Dashboard interactivo
│   │
│   └── utils/                         # Utilidades
│       ├── __init__.py
│       ├── config.py                  # Configuraciones
│       ├── logger.py                  # Sistema de logs
│       └── helpers.py                 # Funciones auxiliares
│
├── scripts/                           # Scripts ejecutables
│   ├── recolectar_resenas.py          # Recolectar reseñas (Outscraper/HasData)
│   ├── descargar_respaldo.py          # Descargar dataset de respaldo de Kaggle
│   ├── preprocess_all.py              # Preprocesar todo el corpus
│   ├── run_pos_tagging.py             # Ejecutar POS tagging
│   ├── generate_metrics.py            # Generar todas las métricas
│   └── create_dashboard.py            # Crear dashboard
│
├── dashboard/                         # Aplicación web (Streamlit/Dash)
│   ├── app.py                         # Aplicación principal
│   ├── pages/                         # Páginas del dashboard
│   │   ├── home.py
│   │   ├── pos_distributions.py
│   │   ├── polarity_comparison.py     # Positivas vs negativas
│   │   └── place_comparison.py        # Por tipo de lugar
│   │
│   └── assets/                        # Recursos estáticos
│       ├── styles.css
│       └── logo.png
│
├── tests/                             # Tests unitarios
│   ├── __init__.py
│   ├── test_loader.py
│   ├── test_pos_tagging.py
│   ├── test_metrics.py
│   └── test_visualization.py
│
├── docs/                              # Documentación
│   ├── metodologia.md                 # Metodología del proyecto
│   ├── hallazgos.md                   # Principales hallazgos
│   └── referencias.md                 # Referencias y fuentes de datos
│
└── outputs/                           # Outputs finales
    ├── figures/                       # Gráficos finales
    │   ├── pos_distribution_positivas.png
    │   ├── pos_distribution_negativas.png
    │   └── comparacion_lugares.png
    │
    ├── tables/                        # Tablas de resultados
    │   └── summary_metrics.csv
    │
    └── reports/                       # Reportes generados
        └── informe_final.pdf

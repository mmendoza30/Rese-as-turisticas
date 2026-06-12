# Uso de Inteligencia Artificial en el Desarrollo del Proyecto Reseñas Turisticas de Costa Rica

**Autores:** Mendoza Morales Mónica · Contreras Artavia Fernando
**Curso:** Minería de textos — BD-163 · Colegio Universitario de Cartago · 2026

---
## 1. Qué herramientas de IA se utilizaron y para qué tareas específicas 

Durante el desarrollo del proyecto Reseñas Turisticas de Costa Rica para minería de textos, utilizamos diferentes asistentes de inteligencia artificial para agilizar la codificación, resolver problemas técnicos y apoyar en la interpretación de resultados. A continuación, se detalla el uso por parte del equipo.

**Herramientas utilizadas:** Gemini, deepseek, chatgpt

---

### Estructuración del Proyecto y Arquitectura del Pipeline

La IA fue utilizada para definir la estructura general del proyecto, incluyendo la organización de carpetas, la separación de etapas (ingesta, EDA, preprocesamiento y modelado) y la convención de nombres de los archivos. Esto permitió trabajar de forma ordenada y mantener consistencia durante todo el desarrollo.

**Aporte:** Se logró una arquitectura clara, modular y escalable desde el inicio del proyecto.


---

### Desarrollo del Pipeline de Datos (Ingesta y Análisis Exploratorio)

Se utilizó IA para generar el código base de los scripts encargados de cargar datos, detectar valores nulos, identificar outliers y generar análisis exploratorios. También se apoyó en la exportación de resultados en formato JSON.

**Aporte:** Automatización del análisis de datos y generación de salidas estructuradas listas para visualización.

---

### Resolución de Errores y Depuración de Código

Durante el desarrollo, la IA fue utilizada para interpretar errores de ejecución, especialmente relacionados con tipos de datos, encoding y librerías. Se empleó para corregir problemas y optimizar el funcionamiento del pipeline.

**Aporte:** Reducción del tiempo de depuración y solución eficiente de errores técnicos.

---

### Generación del Dashboard Interactivo

La IA apoyó en la creación de un dashboard con Plotly Dash que incluye:
- Gráficos de distribución POS con filtros interactivos.
- Comparación de métricas por polaridad y tipo de lugar.
- Estilos profesionales con temática inspirada en Costa Rica (colores verde selva, azul mar, etc.).
- 
**Aporte:** Obtención de una herramienta visual funcional y atractiva para presentar los resultados.


## 2. Ejemplos de prompts utilizados  

---
Necesito de tu ayuda con base a este document adjuntado me ayudes a hacer el contenido para un readme de GitHub, este es el proyecto que debo realizar y los datos que estamos usando son de varios lugares de Costa Rica(Hoteles, Restaurantes y otros lugares)
Los creadores de este proyecto son: Fernando Contreras y Mónica Mendoza
---
Estoy trabando con un corpus en espanol, como puedo entrenar al etiquetador de NLTK para esto?
---
Cómo puedo realizer un proceso de identificacion de sustantivos dependiendo del tagger y los verbos?
---
Cuales son las formulas para realizer el calculo de metricas derivadas (ratio N/V, densidad léxica)
---
Cómo puedo hacer un dashboard interactivo utilizando la libreria de Plotly
---
Ayudame dando una posible estructura para generar un markdown de documentacion de metologia ordenada para un Proyecto
---


## 3. Reflexión sobre cómo la IA ayudó en el aprendizaje  

---
El uso de la IA nos proporcionó claridad sobre la mejor organización del código, el uso correcto de librerías como spaCy y NLTK, los pasos a seguir para construir un pipeline completo de PLN y cómo realizar cálculos estadísticos desconocidos hasta el momento (densidad léxica, ratio N/V). Además, nos permitió entender las diferencias entre sistemas de etiquetas (Universal POS vs. Penn Treebank) y justificar por qué spaCy es más adecuado para el español.
Gracias a la IA, aprendimos a depurar errores de forma más eficiente, a estructurar un proyecto modular y a crear visualizaciones interactivas profesionales. También nos ayudó a redactar documentación técnica y a mantener un repositorio ordenado en GitHub.
---

## 4. Qué modificaciones se hicieron al código/análisis generado por IA  

---
Corrección del tagger de NLTK: El código inicial usaba nltk.pos_tag() (tagger en inglés). Lo modificamos para emplear self.tagger_nltk.tag() entrenado con cess_esp.
Ajuste de rutas de archivos: La IA sugería rutas fijas; nosotros implementamos una función buscar_csv() que busca dinámicamente el archivo en múltiples niveles de directorio.
Personalización del CSS: Los estilos básicos proporcionados fueron reemplazados por una paleta de colores inspirada en Costa Rica (verde selva, azul mar, arena) y se añadieron sombras, bordes redondeados y tipografía profesional.
Optimización de métricas: Las fórmulas de ratio N/V y densidad léxica se ajustaron para manejar correctamente los casos donde no hay verbos o la lista de tokens está vacía.
Modularización: Separamos las funciones de análisis en src/analysis/ y las páginas del dashboard en dashboard/pages/ para mantener el proyecto ordenado y reutilizable.

Estas modificaciones aseguraron que el código final fuera funcional, legible y estuviera completamente adaptado a nuestro corpus y objetivos.
---



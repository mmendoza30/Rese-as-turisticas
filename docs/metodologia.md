# Metodología del proyecto

Para  este proyecto se el **Procesamiento de Lenguaje Natural (NLP)** de datos turísticos para analizar la estructura morfosintáctica de reseñas turísticas de Costa Rica.

El proceso se estructuró en las siguientes fases consecutivas:

---

## 1. Recolección y Limpieza de Datos
En esta primera etapa, se consolidó un corpus de datos que contenía tanto las reseñas textuales emitidas por los usuarios como los atributos geográficos y detalles de interés turístico. 
* **Limpieza:** Se eliminaron registros duplicados, valores nulos y comentarios con valores no valiosos como emojis.
* **Normalización:** El texto de las reseñas fue estandarizado mediante la conversión a minúsculas y la eliminación de caracteres especiales.

---

## 2. Etiquetado Gramatical
Se aplicaron técnicas avanzadas de NLP:
* **Segmentación por Sentimiento:** Las opiniones se dividieron en dos mundos: reseñas con polaridad positiva y reseñas con polaridad negativa.
* **Extracción POS:** Se utilizó un modelo de etiquetado gramatical para cuantificar la distribución porcentual de las categorías morfológicas principales: Sustantivos (`NOUN`), Determinantes (`DET`), Adjetivos (`ADJ`), Adposiciones (`ADP`) y Verbos (`VERB`). 
* **Evidencia Visual:** Este análisis permitió la generación de las distribuciones cuantitativas que se detallan en los graficos `pos_distribution_positivas.png` y `pos_distribution_negativas.png` para tener un mejor detalle de los resultados.

---

## 3. Análisis Comparativo de Atributos Turísticos
Se realizó un analisis de comparación
* **Categorización:** Los datos se agruparon bajo tres destinos clave: *hoteles*, *restaurantes* y *parques nacionales*.
* **Cálculo de Variables:** Se calculó el promedio de la métrica de radio de influencia para determinar el alcance y comportamiento logístico/comercial de cada tipo de lugar.

---
## Resumen
Este estudio permitió observar las preferencias y disgustos de los usuarios. Y ver los comportamientos de los usuarios.
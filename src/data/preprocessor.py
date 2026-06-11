"""
Modelo de preprocesador y la tokenizacion de todas las reseñas anteriormente obtenidas
Herramientasa  utilizar NLTK y spaCy
"""
import pandas as pd
import spacy
import nltk
from typing import List, Tuple

class tokenizacion:
    def __init__(self):
        #Se realiza la carga del modelo a utilizar: es_core_news_md utilizando Spacy
        #Instalacion del recursos necesarios de NLTK
        #nltk.download('punkt_tab')
        #nltk.download('cess_esp')

        #Se debe cargar un corpus en español para entrenar al etiquetador de NLTK
        from nltk.corpus import cess_esp
        entrenamiento = cess_esp.tagged_sents()

        #Creacion de un propio tagger en español
        print("Entrenando el etiquetador de NLTK para español...")
        self.tagger_nltk = nltk.UnigramTagger(entrenamiento)

        self.nlp = spacy.load('es_core_news_md')

    #En este modelo lo que se hara es una funcion donde al final se retorne una lista con el token y lema, utilizando spacy
    def proceso_tokenizacion_spacy(self, texto):
        #Se valida que la reseña contenga un texto
        if pd.isna(texto) or str(texto).strip() == "":
            return []
        #Procesamiento con el pipeline de spacy
        archivo = self.nlp(str(texto))
        #Se guardan las tuplas de token y lema
        lista = []
        for token in archivo:
            lista.append((token.text,token.lemma_))
        return lista


    # En este modelo lo que se hara es una funcion donde al final se retorne una lista con el token,utilizando nltk
    #NLTK lo que hace es separar de una manera directa las palabras
    def proceso_tokenizacion_nltk(self, texto):
        # Se valida que la reseña contenga un texto
        if pd.isna(texto) or str(texto).strip() == "":
            return []
        #
        pl = nltk.word_tokenize(str(texto),language='spanish')
        return nltk.pos_tag(pl)

    #Se le realiza el prceso de tokenizacion a todo el dataframe con las dos herramientas creadas anteriormente
    def proceso_tokenizacion(self, df, column: str = 'reseña'):
        df_rst = df.copy()
        print("[PREPROCESSOR] Se esta aplicando el proceso de tockenización de Spacy Y NLTK")
        df_rst["tokens_spacy"] = df_rst[column].apply(self.proceso_tokenizacion_spacy)
        df_rst["tokens_nltk"] = df_rst[column].apply(self.proceso_tokenizacion_nltk)
        print("Se ha realizado de manera exitosa el proceso de tokenizacion")
        df_rst.to_csv("../../data/processed/resenas_pos_tagged.csv", index=False)
        return df_rst


if __name__ == "__main__":
    from pathlib import Path

    #Se llama el archivo que creo cleaner
    ruta_clean = Path(__file__).resolve().parent.parent.parent / 'data' / 'processed' / 'resenas_clean.csv'

    if ruta_clean.exists():
        df = pd.read_csv(ruta_clean)
        preprocesador = tokenizacion()
        #Se realiza la prueba de tokenizacion
        df_procesado = preprocesador.proceso_tokenizacion(df)

        print("\nEjemplo de salida de spaCy (Token, Lema):")
        print(df_procesado['tokens_spacy'].iloc[0])

        print("\nEjemplo de salida de NLTK (Tokens):")
        print(df_procesado['tokens_nltk'].iloc[0])
    else:
        print(f"No se encontró el archivo limpio en {ruta_clean}. Corre primero cleaner.py")
import pandas as pd
import glob

class consolidar_resenas:
    def __init__(self,ruta):
        self.df_ruta = ruta
        self.columnas = ['name','rating','review_text','review_rating']

    def consolidar(self):
        exceles = glob.glob(f'{self.df_ruta}/*.xlsx')
        datos = []

        for doc in exceles:
            df = pd.read_excel(doc, usecols=self.columnas)
            datos.append(df)
            #df_resenas = pd.merge(df_resenas,df,on=columnas,how='outer')

        df_resenas = pd.concat(datos, ignore_index=True)
        df_resenas.to_csv('data/raw/final/resenas_google_maps.csv', index=False,encoding='utf-8')
        print(f"Se unieron los datos de manera exitosa {len(df_resenas)}")
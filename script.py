## cargue de librerias
import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import os

## cargue del dataset

mainpath = 'Python/datasets/'
filename1 = "medellin-apartamento-arriendo.xlsx"
filename2 = "medellin-casa-arriendo.xlsx"
fullpath1 = os.path.join(mainpath, filename1)
fullpath2 = os.path.join(mainpath, filename2)
df1= pd.read_excel(fullpath1)
df2= pd.read_excel(fullpath2)
# concatenar los dos dataset
df3= pd.concat([df1,df2])
df3.head(10)
## Limpieza de datos- Mineria
df3['antigüedad'] = df3['antigüedad'].str.replace("Antigüedad",'')
df3['antigüedad'] = df3['antigüedad'].str.replace("'",'')
df3['area Costruida'] = df3['area Costruida'].str.replace('Área construida','')
df3['area Costruida'] = df3['area Costruida'].str.replace(" '",'')
df3['area Costruida'] = df3['area Costruida'].str.replace(" m²'",'')
df3['area Costruida'] = df3['area Costruida'].str.replace('null','')
df3['area privada'] = df3['area privada'].str.replace('Área privada','')
df3['area privada'] = df3['area privada'].str.replace("'",'')
df3['area privada'] = df3['area privada'].str.replace(" m²",'')
df3['area privada'] = df3['area privada'].str.replace(' null','')
df3['valor arriendo'] = df3['valor arriendo'].str.replace("Valor arriendo",'')
df3['valor arriendo'] = df3['valor arriendo'].str.replace("$",'',regex=True)
df3['valor arriendo'] = df3['valor arriendo'].str.replace("'",'',regex=True)
df3['valor arriendo'] = df3['valor arriendo'].str.replace(".",'',regex=True)
df3['valor administracion'] = df3['valor administracion'].str.replace("Valor administración",'')
df3['valor administracion'] = df3['valor administracion'].str.replace("$",'',regex=True)
df3['valor administracion'] = df3['valor administracion'].str.replace("'",'',regex=True)
df3['valor administracion'] = df3['valor administracion'].str.replace(".",'',regex=True)
df3['parqueaderos'] = df3['parqueaderos'].str.replace("Parqueaderos",'')
df3['parqueaderos'] = df3['parqueaderos'].str.replace("'",'',regex=True)
df3['parqueaderos'] = df3['parqueaderos'].str.replace("]",'',regex=True)
df3['parqueaderos'] = df3['parqueaderos'].str.replace("'",'',regex=True)
df3['parqueaderos'] = df3['parqueaderos'].str.replace('"','',regex=True)
df3['parqueaderos'] = df3['parqueaderos'].str.replace('"','',regex=True)
df3['parqueaderos'] = df3['parqueaderos'].str.replace(' ','',regex=True)
df3['parqueaderos'] = df3['parqueaderos'].str.replace('0','',regex=True)
df3['Habitaciones'] = df3['Habitaciones'].str.replace("Habitaciones",'')
df3['Habitaciones'] = df3['Habitaciones'].str.replace("'",'')
df3['Habitaciones'] = df3['Habitaciones'].str.replace("]",'',regex=True)
df3['Habitaciones'] = df3['Habitaciones'].str.replace('"','',regex=True)
df3['Habitaciones'] = df3['Habitaciones'].str.replace('"','',regex=True)
df3['baños'] = df3['baños'].str.replace("Baños",'')
df3['baños'] = df3['baños'].str.replace("'",'')
df3['baños'] = df3['baños'].str.replace("]",'',regex=True)
df3['baños'] = df3['baños'].str.replace("'",'')
df3['baños'] = df3['baños'].str.replace('"','',regex=True)
df3['baños'] = df3['baños'].str.replace('"','',regex=True)
df3['estrato'] = df3['estrato'].str.replace('Estrato','')
df3['estrato'] = df3['estrato'].str.replace("]",'',regex=True)
df3['estrato'] = df3['estrato'].str.replace(" '",'')
df3['estrato'] = df3['estrato'].str.replace('"','',regex=True)
df3['estrato'] = df3['estrato'].str.replace(' null','',regex=True)
df3['estrato'] = df3['estrato'].str.replace("'",'')
df3['estrato'] = df3['estrato'].str.replace('null','',regex=True)
df3['location'] = df3['location'].str.upper()
df3['location'] = df3['location'].str.replace('Á','A')
df3['location'] = df3['location'].str.replace('É','E')
df3['location'] = df3['location'].str.replace('Í','A')
df3['location'] = df3['location'].str.replace('Ó','A')
df3['location'] = df3['location'].str.replace('Ú','A')
## Transforma tipo de variables


df3['area Costruida'] = pd.to_numeric(df3['area Costruida'],errors = 'coerce')
df3['area privada'] = pd.to_numeric(df3['area privada'],errors = 'coerce')
df3['valor arriendo'] = pd.to_numeric(df3['valor arriendo'],errors = 'coerce')
df3['parqueaderos'] = pd.to_numeric(df3['parqueaderos'],errors = 'coerce')
df3['Habitaciones'] = pd.to_numeric(df3['Habitaciones'],errors = 'coerce')
df3['baños'] = pd.to_numeric(df3['baños'],errors = 'coerce')
df3['estrato'] = pd.to_numeric(df3['estrato'],errors = 'coerce')

# remueve las columnas lat y long
df3 = df3.drop(columns=['A','B'])
df4 = df3[(df3.price != 1)]

print(df3.info())


df3.head(10)

## copiar archivo
df3.to_excel("/Python/datasets//Data set.xlsx")

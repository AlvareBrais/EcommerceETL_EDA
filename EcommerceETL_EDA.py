# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 18:30:34 2023

Proyecto data analytics//data scientist

@author: Brais


Se nos da un data set con informacion de 3 años sobre un Ecommerce de joyeria, nos piden analisis exploratorio. (EDA)
"""
#Importamos los modulos necesarios
import pandas as pd #Para el procesado de datos, archivos csv en este caso
import numpy as np #algebra linear

archivo_csv = "jewelry.csv"

df = pd.read_csv(archivo_csv)

#Realizamos el analisis exploratorio

#Mostramos las primeras filas para ver un poco la estructura del documento.

print("Primeras filas del df")
print(df.head())


#Mostramos la informacion general del df
#\n al principio del print para aplicar un espacio en blanco entre las muestras del df

print("\nInformación general del DataFrame:")
print(df.info())


#Estadisticas descriptivas ( describen de manera global el conjunto de datos, media, mediana, percentiles etc)
print("\nEstadisticas descriptivas")
print(df.describe())

print(df.columns)


#He visto algo que no esta muy bien en estos datos, vamos a arreglarlo.

#Fase de procesamiento de datos.
#Los nombres de las columnas no son nada intuitivos, los vamos a cambiar.

# Renombrar y reordenar las columnas
df = df.rename(columns={
    '2018-12-01 11:40:29 UTC': 'Order_Datetime',
    '1924719191579951782': 'Order_ID',
    '1842195256808833386': 'Product_ID',
    '1': 'Quantity',
    '1806829201890738522': 'Category_ID',
    'jewelry.earring': 'Category_Alias',
    '0': 'Brand_ID',
    '561.51': 'Price_USD',
    '1515915625207851155': 'User_ID',
    'Unnamed: 9': 'Product_Gender',
    'red': 'Main_Color',
    'gold': 'Main_Metal',
    'diamond': 'Main_Gem'
})

# Reordenar las columnas
column_order = ['Order_Datetime', 'Order_ID', 'Product_ID', 'Quantity', 'Category_ID', 'Category_Alias', 'Brand_ID', 'Price_USD', 'User_ID', 'Product_Gender', 'Main_Color', 'Main_Metal', 'Main_Gem']
df = df[column_order]

print("\nComprobamos los cambios en las columnas")
print(df.columns)

#Ya se puede leer mas facil este dataset, sigamos.


print(df.info)

print("\nBuscamos valores nulos:")
print()

print(df.isna().sum())

#Obsero que hay un numero de nulos no muy relevante en las columnas Category_Id y Category_alias.
#A nivel practica vamos a eliminarlos, ya que no afectaran a la estadisticas globales pero si nos pueden dar problemas



















#Otra opcion hubiera sido añadir valores de la media o mediana













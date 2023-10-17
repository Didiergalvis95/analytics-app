import pandas as pd
from helpers.crearCsv import crearCSV
from data.ventas import ventas, encabezados

#crear un CSV con los datos
crearCSV(ventas, 'venta.csv', encabezados)

# cargo la fuente de datos y cro un dataframe
ventasDataFrame = pd.read_csv('data/venta.csv')
#print(ventasDataFrame)

# explorar datos 
examenUno = ventasDataFrame.head()
examenDos = ventasDataFrame.tail()
examentres = ventasDataFrame.head(20)
examenCuatro = ventasDataFrame.info()
examenCinco = ventasDataFrame.describe()
examenSeis = ventasDataFrame.tail(50)


# presentar y exportar los datos
print(examenUno)
print("\n")
print(examenDos)
print("\n")
print(examentres)
print("\n")
print(examenCuatro)
print("\n")
print(examenCinco)
print("\n")
print(examenSeis)
print("\n")
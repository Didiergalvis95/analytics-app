import pandas as pd
from helpers.crearCsv import crearCSV
from data.ventas import ventas, encabezadoVentas
from helpers.crearTablaHTML import crearTabla

#crear un CSV con los datos
crearCSV(ventas, 'venta.csv', encabezadoVentas)

# cargo la fuente de datos y cro un dataframe
ventasDataFrame = pd.read_csv('data/venta.csv')

#print(ventasDataFrame)
crearTabla(ventasDataFrame, 'tablaventas')

# explorar datos 
'''examenUno = ventasDataFrame.head()
examenDos = ventasDataFrame.tail()
examentres = ventasDataFrame.head(20)
examenCuatro = ventasDataFrame.info()
examenCinco = ventasDataFrame.describe()
examenSeis = ventasDataFrame.tail(50) '''

# filtrar y ordear
fltroUno  = ventasDataFrame.query("(Costo>=2900000) and (Costo<=3000000)")
filtroventas = ventasDataFrame.query("(Costo>600000)")
filtroventasDos = ventasDataFrame.query("(Costo > 100000) and (Costo < 600000)")
totalVentas = filtroventas[['OrdenCompra', 'Costo']]

print(totalVentas)
crearTabla(totalVentas, 'tablaFiltroVentas')
#print(filtroventasDos)

# presentar y exportar los datos



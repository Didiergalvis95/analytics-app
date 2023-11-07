import pandas as pd
import matplotlib.pyplot as plt
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

crearTabla(totalVentas, 'tablaFiltroVentas')
#print(filtroventasDos)

# presentar y exportar los datos
ventasAltas = ventasDataFrame.nlargest(5, 'Costo')
ventasBajas = ventasDataFrame.nsmallest(5, 'Costo')
print(ventasBajas)

#Graficos
ventasAltas["OrdenCompra"]=ventasAltas["OrdenCompra"].astype(str)
colores = ['red', 'green', 'blue']
plt.figure(figsize=(10, 10))
plt.bar(ventasAltas['Cliente'], ventasAltas['Costo'], color=colores)

#personalizando graficos
plt.xlabel("Cliente")
plt.ylabel("Costo")
plt.title("Ventas mas altas")
plt.xticks(rotation=45)

rutaGrafico = "figures/ventas.png"
plt.savefig(rutaGrafico)
import pandas as pd
from helpers.crearCsv import crearCSV
from data.productos import productos, encabezadoProductos
from helpers.crearTablaHTML import crearTabla

crearCSV(productos, 'producto.csv', encabezadoProductos)
productosDataFrame = pd.read_csv('data/producto.csv')
crearTabla(productosDataFrame, 'tablaproductos')

filtroProductos = productosDataFrame.query("Costo > 500000")
filtroProductosDos = productosDataFrame.query("(Costo > 0) and (Costo < 150000)")

totalproductos = filtroProductos[['Id', 'Nombre', 'Costo']]

crearTabla(totalproductos, 'tablaFiltroProductos')
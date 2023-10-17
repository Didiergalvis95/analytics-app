import pandas as pd
from helpers.crearCsv import crearCSV
from data.empleados import empleados, encabezados

crearCSV(empleados, 'empleados.csv', encabezados)
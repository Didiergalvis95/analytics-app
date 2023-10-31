import pandas as pd
from helpers.crearCsv import crearCSV
from data.empleados import empleados, encabezadoEmpleados
from helpers.crearTablaHTML import crearTabla


crearCSV(empleados, 'empleado.csv', encabezadoEmpleados)
empleadosDataFrame = pd.read_csv('data/empleado.csv')
print(empleadosDataFrame)
crearTabla(empleadosDataFrame, 'tablaempleados')


filtroEmpleados = empleadosDataFrame.query("Edad < 24")
filtroEmpleadosDos = empleadosDataFrame.query("Edad > 58")
filtroEmpleadosTres = empleadosDataFrame.query("(Cargo == 'Desarrollador Junior')")
filtroEmpleadosCuatro = empleadosDataFrame.query("Salario > 2500000")
totalEmpleados = filtroEmpleadosTres[['Nombre', 'Apellido', 'Cargo']]

print(totalEmpleados)


crearTabla(totalEmpleados, 'tablaFiltroEmpleados')

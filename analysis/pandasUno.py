import pandas as pd
from data.empleados import datosEmpleados

ciudades =['Jerusalen', 'Telabit', 'kiev', 'Itagui', 'Pitalito']

DataFrameCiudades = pd.DataFrame({'Ciudad':ciudades})
from data.empleados import datosEmpleados

print(DataFrameCiudades)

estudiantes=[
    {'id':1,
     'nombre': 'Mariana Cuervo',
     'promedio': 0.0
    },
    {'id':2,
     'nombre': 'Matias Gonzales',
     'promedio': 0.5
    },
    {'id':3,
     'nombre': 'Camilo Garcia',
     'promedio': 2.0
    },
    {'id':4,
     'nombre': 'Steven Barrientos',
     'promedio': 1.8
    },
    {'id':5,
     'nombre': 'Isabela londoño',
     'promedio': 0.0
    }
]

DataFrameEstudiantes = pd.DataFrame(estudiantes)

print(DataFrameEstudiantes)


'''datosEmpleados = pd.DataFrame(listEmpleados)
print(datosEmpleados)
'''

import random as rd

nombres = [
    'Juan', 'María', 'Carlos', 'Laura', 'José', 'Ana', 'Pedro', 'Isabel',
    'Luis', 'Sofía', 'Andrés', 'Lucía', 'Javier', 'Carmen', 'Miguel', 'Elena',
    'Ricardo', 'Patricia', 'Fernando', 'Silvia'
]
apellidos = ['Carvajal Casillas', 'Arisizabal Florez', 'González Pérez', 'Rodríguez López',
    'Martínez Sánchez', 'Fernández González', 'López Pérez', 'Díaz García',
    'Hernández Rodríguez', 'Gómez Pérez', 'Pérez García', 'Sánchez López',
    'Ramírez López', 'Torres Sánchez', 'Díaz Martínez', 'Fernández Pérez',
    'Torres Rodríguez', 'Sánchez García', 'García Díaz', 'López González'
]


encabezadoEmpleados = ['Id', 'Nombre', 'Apellido', 'Salario', 'Deudas', 'Edad', 'Retefuente', 'Correo', 'Telefono',  'Cargo']
empleados = []
for _ in range(3000):
    id = rd.randint(0, 100)
    nombre = rd.choice(nombres)
    apellido = rd.choice(apellidos)
    salario = rd.randint(1160000, 18000000)
    deudas = rd.choice([True, False])
    retefuente = 1 if salario > 6000000 else 0
    edad = rd.randint(22, 60)
    correo = nombre+ str(edad)+"@correo.com"
    numero_telefono = rd.randint(5469832605, 9681005893)
    cargo = rd.choice(['Desarrollador Junior', 
    'Desarrollador Intermedio', 
    'Arquitecto', 
    'Desarrollador Avanzado'
    ])
    empleado = [id, nombre, apellido, salario, deudas, edad, retefuente, correo, numero_telefono, cargo ]
    empleados.append(empleado)

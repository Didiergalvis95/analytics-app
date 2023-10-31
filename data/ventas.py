import random as rd
from data.empleados import nombres, apellidos
encabezadoVentas=['OrdenCompra', 'Cliente', 'Costo']
ventas = []
for _ in range(2000):
    ordenCompra = rd.randint(0,5000)
    nombre = rd.choice(nombres)
    apellido = rd.choice(apellidos)
    cliente = nombre + " " + apellido
    costo = rd.randint(150000, 800000)
    orden = [ordenCompra, cliente, costo]
    ventas.append(orden)

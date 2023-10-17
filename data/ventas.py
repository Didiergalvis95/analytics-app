import random as rd
encabezados=['OrdenCompra', 'Cliente', 'Costo']
ventas = []
for _ in range(1000):
    ordenCompra = rd.randint(0,5000)
    cliente = rd.choice(['Andres', 'Ana', 'Isabel', 'Pablo', 'Juan', 'Mariana', 'Matias'])
    costo = rd.randint(1160000, 18000000)
    orden = [ordenCompra, cliente, costo]
    ventas.append(orden)
print(ventas)
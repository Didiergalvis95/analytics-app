import random as rd
nombresProductos = [
    'Smartphone', 'Laptop', 'Auriculares inalámbricos', 'Televisor LED',
    'Cámara digital', 'Altavoz Bluetooth', 'Reloj inteligente', 'Tableta',
    'Impresora láser', 'Refrigerador', 'Cafetera', 'Licuadora',
    'Juego de sartenes', 'Máquina de ejercicio', 'Bicicleta de montaña',
    'Zapatos deportivos', 'Vestido de noche', 'Perfume', 'Gafas de sol', 'Maleta de viaje'
]
encabezadoProductos = ['Id','Nombre', 'Costo','iva']
productos = []

for _ in range(2000):
    id = rd.randint(2698, 5432)
    nombre = rd.choice(nombresProductos)
    costo = rd.randint(50000, 800000)
    iva = costo * 0.19
    producto = [id,nombre, costo, iva]
    productos.append(producto)
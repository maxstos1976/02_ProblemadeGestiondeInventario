# Gestion de Inventario
# Imagina que tabajas en un empresa de logistica y tu tarea es desarrollar un sistema de control de inventario. 
# El inventario esta representado por una lista de productos ordenados por sus codigos. Cada producto se describe
# como un diccionario con las claves 'codigo' y'cantidad'. Tu objectivo es implementar una funcion recursiva que realice
# una busqueda binaria en este inventario y devuelva la cantidad deisponible para um productor especifico, dado su codigo.

def buscar_cantidad_producto(inventario, codigo_producto, inicio = 0, fin = None):
    if fin is None:
        fin = len(inventario) - 1
    #caso base: si el rango no es valido
    if inicio > fin:
        return 0
    
    print(f'Buscando {codigo_producto} en rango {inicio} - {fin}')
    medio = (inicio + fin) // 2
    
    #comparar el codigo del producto con el codigo de la posicion media
    if inventario[medio]['codigo'] == codigo_producto:
        #caso base PRIMERO
        return inventario[medio]['cantidad']
    elif inventario[medio]['codigo'] < codigo_producto:
        #caso recursivo - el codigo va a estar en el lado derecho del inventario
        return buscar_cantidad_producto(inventario, codigo_producto, medio+1, fin)
    else:
        #caso recursivo - el codigo va a estar en el lado izquierdo del inventario
        return buscar_cantidad_producto(inventario, codigo_producto, inicio, medio-1)

# Declarar inventario

inventario = [
    {'codigo': 101, 'cantidad': 60},
    {'codigo': 204, 'cantidad': 40},
    {'codigo': 307, 'cantidad': 20},
    {'codigo': 412, 'cantidad': 40},
    {'codigo': 501, 'cantidad': 60},
    {'codigo': 601, 'cantidad': 60},
    {'codigo': 704, 'cantidad': 40},
    {'codigo': 807, 'cantidad': 20},
    {'codigo': 912, 'cantidad': 40},
    {'codigo': 1001, 'cantidad': 60}
]

codigo_producto = int(input('Ingrese el codigo del producto: '))
cantidad = buscar_cantidad_producto(inventario, codigo_producto)
print(f'La cantidad disponible para el producto con codigo {codigo_producto} es {cantidad}')
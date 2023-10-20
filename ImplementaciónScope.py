import ast

# Definición de una tabla de símbolos para almacenar información de funciones
tabla_de_simbolos = []

# Función para recorrer el árbol sintáctico en busca de funciones
def encontrar_funciones(node, ambito):
    if isinstance(node, ast.FunctionDef):
        # Si el nodo es una definición de función, registramos la función en la tabla de símbolos
        funcion = {
            "nombre": node.name,
            "tipo": "función",
            "ambito": ambito
        }
        tabla_de_simbolos.append(funcion)

    # Recorremos los nodos hijos del nodo actual
    for child_node in ast.iter_child_nodes(node):
        encontrar_funciones(child_node, ambito)

# Código fuente de ejemplo (puedes reemplazarlo con tu propio código)
codigo_fuente = """
def funcion1():
    pass

variable = 42

def funcion2():
    pass
"""

arbol_sintactico = ast.parse(codigo_fuente)

encontrar_funciones(arbol_sintactico, "global")

# Imprimimos la tabla de símbolos
print("Tabla de símbolos:")
for simbolo in tabla_de_simbolos:
    print(f"Nombre: {simbolo['nombre']}, Tipo: {simbolo['tipo']}, Ámbito: {simbolo['ambito']}")
  

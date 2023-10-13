import pandas as pd

class node_stack:
    def __init__(self, symbol, lexeme):
        self.symbol = symbol
        self.lexeme = lexeme

class node_tree:
    def __init__(self, id, symbol, lexeme):
        self.id = id
        self.symbol = symbol
        self.lexeme = lexeme
        self.children = []
        self.father = None

tabla = pd.read_csv("tabla.csv", index_col=0)

stack = []
count = 0

stack.append('$')

def analizador_sintactico(input_tokens):
    global count
    stack.append('E')  
    input_index = 0 
    
    while len(stack) > 0:
        top_of_stack = stack[-1]
        
        current_token = input_tokens[input_index]["symbol"]
        
        if top_of_stack == current_token:
            stack.pop()
            input_index += 1
        else:
            production = tabla.loc[top_of_stack, current_token]
            
            if isinstance(production, str) and production == 'e':
                stack.pop()
            else:
                stack.pop()
                for symbol in reversed(production.split()):
                    stack.append(symbol)
                
        print("Pila:", stack)
        print("Entrada:", [token["symbol"] for token in input_tokens[input_index:]])
    
    if input_index == len(input_tokens) and len(stack) == 0:
        print("Análisis sintáctico exitoso.")
    else:
        print("Error en el análisis sintáctico.")

input_tokens = [ 
    {"symbol":"int", "lexeme":"4", "nroline":2, "col":2},
    {"symbol":"*", "lexeme":"*", "nroline":2, "col":4},
    {"symbol":"int", "lexeme":"5", "nroline":2, "col":6},
    {"symbol":"$", "lexeme":"$", "nroline":0, "col":0},
]

analizador_sintactico(input_tokens)


# https://onlinegdb.com/VT7gU6BgH


# https://onlinegdb.com/t_-tad6Je

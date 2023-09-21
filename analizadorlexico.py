# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# r'atring' -> r significa que la cadena es tradada sin caracteres de escape, 
# es decir r'\n' seria un \ seguido de n (no se interpretaria como salto de linea) 

 # List of token names.   This is always required
reserved = {
    'walabi'        : 'TIPO_WHILE',
    'dodo'          : 'TIPO_DOWHILE',
    'flamenco'      : 'TIPO_FOR',
    'pantera'       : 'PRINT',
    'rana'          : 'READ',
    'iguana'        : 'IF',
    'elefante'      : 'ELSE',
    'salmon'        : 'SHORT',
    'ibice'         : 'TIPO_INT',
    'foca'          : 'FLOAT',
    'chivo'         : 'CHAR',
    'vaca'          : 'VOID',
    'bisonte'       : 'BOOL',
    'rayas'         : 'RETURN'
}

tokens = [
    'NUM',
    'REAL',
    'OPER_SUMA',
    'OPER_RESTA',
    'OPER_MUL',
    'OPER_DIV',
    'OPER_RESTO',
    'SIG_MAYOR',
    'SIG_MENOR',
    'SIG_MAYORIGUAL',
    'SIG_MENORIGUAL',
    'SIG_IGUAL',
    'OPER_IGUALDAD',
    'OPER_DIFER',
    'PARENT_INICIO',
    'PARENT_FIN',
    'LL_INICIO',
    'LL_FIN',
    'CORCH_INICIO',
    'CORCH_FIN',
    'COMA',
    'PUNT_COMA',
    'PUNTO',
    'DOS_PUNTOS',
    'ID',
    'COMILLA_SIMPLE',
    'COMILLA_DOBLE',
    'OPER_DESPLA_IZ',
    'OPER_DESPLA_DE'
    
 ] + list(reserved.values())
 
 # Regular expression rules for simple tokens
t_OPER_SUMA    = r'\+'
t_OPER_RESTA   = r'-'
t_OPER_MUL   = r'\*'
t_OPER_DIV  = r'/'
t_OPER_RESTO = r'%'
t_SIG_MAYOR = r'>'
t_SIG_MENOR = r'<'
t_SIG_MAYORIGUAL = r'>='
t_SIG_MENORIGUAL = r'<='
t_SIG_IGUAL = r'\='
t_OPER_IGUALDAD = r'=='
t_OPER_DIFER = r'!='
t_PARENT_INICIO  = r'\('
t_PARENT_FIN  = r'\)'
t_LL_INICIO = r'\{'
t_LL_FIN = r'\}'
t_CORCH_INICIO = r'\['
t_CORCH_FIN = r'\]'
t_COMA = r'\,'
t_PUNT_COMA = r'\;'
t_PUNTO = r'\.'
t_DOS_PUNTOS = r'\:'
t_COMILLA_SIMPLE = r'\''
t_COMILLA_DOBLE = r'\"'
t_OPER_DESPLA_IZ = r'\<<'
t_OPER_DESPLA_DE = r'\>>'


#t_NUMBER  = r'\d+'
 
 # A regular expression rule with some action code
def t_ID(t):
    r'[a-zA-Z]+ ( [a-zA-Z0-9]* )'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)  # guardamos el valor del lexema  
    #print("se reconocio el numero")
    return t
 
 # Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
 
 # A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
 
 # Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
def t_COMENLINEA(t):
    r'conejo.*'
    pass
 
# Build the lexer
lexer = lex.lex()

# Leer el contenido del archivo externo
archivo_externo = "ejemplo1.txt"  # Reemplaza con el nombre de tu archivo
with open(archivo_externo, "r") as file:
    data = file.read()

# Give the lexer some input
lexer.input(data)

# Tokenize
tokens_line = []
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    tokens_line.append(tok.type)
    
print(" ".join(tokens_line))


# https://onlinegdb.com/IEKGKAr2F

import ply.lex as lex

tokens = [
    "COMMA",
    "EQUALS",
    "GREATER",
    "LESS",
    "LPAREN",
    "RPAREN",
    "VALUE",

    "SELECT",
    "FROM",
    "WHERE",
    "AND",
    "OR",
    "NOT",
    "IN",
]

t_COMMA = r","
t_EQUALS = r"="
t_GREATER = r">"
t_LESS = r"<"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_VALUE = r"\w+"

t_SELECT = r"[Ss][Ee][Ll][Ee][Cc][Tt]"
t_FROM = r"[Ff][Rr][Oo][Mm]"
t_WHERE = r"[Ww][Hh][Ee][Rr][Ee]"
t_AND = r"[Aa][Nn][Dd]"
t_OR = r"[Oo][Rr]"
t_NOT = r"[Nn][Oo][Tt]"
t_IN = r"[Ii][Nn]"

t_ignore = " \t"



def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f"Caracter inválido {t.value[0]}")
    t.lexer.skip(1)



lexer = lex.lex()
frase = "Select id, nome, salario From empregados Where salario >= 820"
lexer.input(frase)

while tok := lexer.token():
    print(tok)

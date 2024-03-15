import math
import sys

import ply.lex as lex
import json
import pandas as pd
import re
from datetime import date

saldo = 0

tokens = (
    "LISTAR",
    "MOEDA",
    "SELECIONAR",
    "SALDO",
    "SAIR"
    
)

def t_LISTAR(t):

    r"LISTAR"
    df = pd.DataFrame(t.lexer.maquinaQuantidades["stock"])
    print("maq:")
    print(df.to_string(index=False))
    print("")
    return t


def t_MOEDA(t):
    r"MOEDA.+\."

    listaMoedas = re.findall(r"(1e|2e|1c|2c|5c|10c|20c|50c)", t.value)
    global saldo

    for moeda in listaMoedas:
        if moeda[-1] == "e":
            saldo += int(moeda[:-1])
        elif moeda[-1] == "c":
            saldo += int(moeda[:-1])/100
    saldo = round(saldo, 2)

    euros, centimos = determinarSaldo(saldo)


    print(f"maq: Saldo = {euros}e{centimos}c\n")
    return t


def t_SALDO(t):
    r"SALDO"
    global saldo
    euros, centimos = determinarSaldo(saldo)
    print(f"maq: Saldo = {euros}e{centimos}c\n")
    return t


def t_SELECIONAR(t):
    r"SELECIONAR\sA[0-9]+"
    global saldo
    valorInput = t.value[11:]
    try:
        valor = valorInput
        artigo = None
        for art in t.lexer.maquinaQuantidades["stock"]:
            if valor == art["cod"]:
                artigo = art
                break

        if artigo is None:
            print("Artigo não existe\n")
        elif artigo["quant"] == 0:
            print("Artigo esgotado\n")
        elif artigo["preco"] > saldo:
            print("maq: Saldo insufuciente para satisfazer o seu pedido")
            euros, centimos = determinarSaldo(saldo)
            euros2, centimos2 = determinarSaldo(artigo["preco"])
            print(f"maq: Saldo = {euros}e{centimos}c; Pedido = {euros2}e{centimos2}c\n")
        else:
            print(f'Pode retirar o produto dispensado "{artigo["nome"]}"')
            saldo -= artigo["preco"]
            artigo["quant"] -= 1
            euros, centimos = determinarSaldo(saldo)
            print(f"maq: Saldo = {euros}e{centimos}c\n")
            with open("maquina.json", 'w', encoding='utf-8') as file:
                json.dump(t.lexer.maquinaQuantidades, file)



    except ValueError:
        print("Valor inserido inválido\n")
    return t


def t_SAIR(t):
    r"SAIR"
    global saldo
    saldoCentimos = saldo * 100
    moedas = [200, 100, 50, 20, 10, 5, 2, 1]
    troco = ""

    for moeda in moedas:
        nMoedas = saldoCentimos//moeda
        if (moeda == 200 or moeda == 100) and nMoedas > 0:
            troco += f"{nMoedas}x {moeda/100}e, "
            saldoCentimos -= nMoedas * moeda
        elif nMoedas > 0:
            troco += f"{nMoedas}x {moeda}c, "
            saldoCentimos -= nMoedas*moeda

    if troco == "":
        print(f"maq: Não há troco.")
    else:
        print(f"maq: Pode retirar o troco: {troco[:-2]}")
    print("maq: Até à próxima")
    sys.exit(0)


t_ignore = " \t"


def determinarSaldo(preco):
    euros = int(preco)
    centimos = round((preco - euros)*100)
    return euros, centimos



def main():
    lexer = lex.lex()
    print(f"maq: {date.today()}, Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.\n")


    while True:

        with open("maquina.json", encoding="utf-8") as file:
            maquinaQuantidades = json.load(file)
            lexer.maquinaQuantidades = maquinaQuantidades

        userInput = input(">> ")

        lexer.input(userInput)
        tok = lexer.token()

        if tok is None:
            print("Comando não reconhecido\n")


def t_error(t):
    # print(f"Caracter inválido {t.value[0]}")
    t.lexer.skip(1)


if "__main__" == __name__:
    main()






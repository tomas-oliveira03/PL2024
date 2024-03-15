# Máquina de Vending

## Autor:

**Nome:** Tomás Barbosa Oliveira

**Id:** a100657

## Trabalho efetuado:

O objetivo do trabalho era criar em Python um pequeno programa que construisse a lógica por detrás de uma máquina de vending.


## Resolução:

Para resolver o problema, decidi utilizar a biblioteca `lex` do Python para poder utilizar analisadores léxicos.

Os artigos foram guardados num json, `maquina.json`.

As expressões usadas têm em consideração os vários inputs que o utilizador coloca, tendo em consiferação as vírgulas, semântica, etc.

Para além do básico, fiz também uma atualização do json cada vez que um artigo era comprado, subtraindo um à quantidade desse mesmo artigo, e também fiz as opções de o stock ser inexistente ou vazio, assim como quando o utilizador não tem saldo. 


**Para correr o programa:** 

```python3 script.py```

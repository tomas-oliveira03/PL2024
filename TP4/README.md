# Analisador Léxico

## Autor:

**Nome:** Tomás Barbosa Oliveira

**Id:** a100657

## Trabalho efetuado:

O objetivo do trabalho era criar em Python um pequeno programa que fizesse o seguinte.

Construir um analisador léxico para uma liguagem de query com a qual se podem escrever frases do género:
`Select id, nome, salario From empregados Where salario >= 820`


## Resolução:

Para resolver o problema, decidi utilizar a biblioteca `lex` do Python para poder utilizar analisadores léxicos.

As expressões usadas têm em consideração a particularidade de que expressões como o `Select` podem aparecer assim também `SELECT` o que me levou a ter em consideração as letras maiúsculas.

De seguida, apenas separei as expressões de sinais de maior, menor ou igual e também separei os valores que as chaves possuiam.


**Para correr o programa:** 

```python3 script.py```

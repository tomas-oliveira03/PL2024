# Somador on/off

## Autor:

**Nome:** Tomás Barbosa Oliveira

**Id:** a100657

## Trabalho efetuado:

O objetivo do trabalho era criar em Python um pequeno programa que fizesse o seginte:

1. Pretende-se um programa que some todas as sequências de dígitos que encontre num texto;
2. Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
3. Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
4. Sempre que encontrar o caráter “=”, o resultado da soma é colocado na saída.

Como não estava explícito no enunciado, considerei que qualquer comando referido acima pode constar no meio de uma string.

## Resolução:

Para resolver o problema, decidi utilizar a biblioteca `re` do Python para poder utilizar expressões regulares. Com essa biblioteca decidi utilizar o método `findall` para encontrar todas as ocorrências de uma determinada expressão regular no ficheiro que é dado como input.

A expressão regular utilizada foi `r'(on|off|=|-?[0-9]+)'`, visto que encontra no texto todas as ocorrências de **on**, **off*, **=** assim como **sequências de dígitos** podendo ser eles negativos ou positivos, com ou sem sinal.

Com o findall dei assim parse a todos esses comandos possíveis, aparecendo de forma cronológica de acordo com o texto numa lista.

Com essa lista criada, fiz um **for loop** de modo a iterar comando a comando e a averiguar que tipo de operação era necessário de fazer. A cada sinal de igual que encontrado é inserido no terminal uma mensagem indicando o resultado até então, assim como no final de tudo é indicado o resultado final.


**Para correr o programa:** 

```python3 main.py input.txt```

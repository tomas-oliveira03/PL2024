# Analisador Sintático

## Autor:

**Nome:** Tomás Barbosa Oliveira

**Id:** a100657

## Trabalho efetuado:

**Linguagem:**


Garantir a prioridade de operadores, garantir que é LL(1) e calcular look aheads.
```
? a
b = a * 2 / (27 - 3)
! a + b
c = a * b / (a/b)
```


## Resolução:

```
Z -> Start '$'

Start -> '?' var {'?'}
    |  var '=' ExpFinal {var}
    |  '!' ExpFinal {'!'}

ExpFinal -> Exp3 Exp2 Exp1 {var, number, '('}

Exp1 -> '+' ExpFinal {'+'}
    |  '-' ExpFinal {'-'}
    |  & {'$', ')'}

Exp2 -> '*' ExpFinal {'*'}
    |  '/' ExpFinal {'/'}
    |  & {'$', ')'}

Exp3 -> '(' ExpFinal ')' {'('}
    |  var {var}
    |  number {number}
```

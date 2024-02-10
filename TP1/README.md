# Análise de um Dataset

## Autor:

**Nome:** Tomás Barbosa Oliveira

**Id:** a100657

## Trabalho efetuado:
O trabalho tinha por objetivo fazer o estudo de um dataset em formato _.csv_ através do **stdin**, e apresentar os respetivos dados no terminal. Foi realizado do seguinte modo:

Para o processamento de dados, decidi utilizar o método _split_ do Python para separar os vários parâmetros de cada linha.

- Para obter uma lista ordenada das várias modalidades optei por criar um _set_ e, no final, ordená-lo.
- Para descobrir as percentagens de aptos e inaptos contei o número de aptos e o número total de atletas, para no final fazer o cálculo em %.
- Para a distribuição em escalões utilizei um dicionário para identificar quantos atletas têm uma determianda idade. Após ler todas as linhas, criei os respetivos escalões com intervalos de 5 unidades, até à idade máxima encontrada e acedi ao dicionário para determinar o números de atletas por escalão. Decidi também apresentar apenas os escalões que têm atletas no seu intervalo.


**Para correr o programa:** 

```python3 script.py < emd.csv```

ou

```cat emd.csv | python3 script.py```


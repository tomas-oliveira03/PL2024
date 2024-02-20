# Transformar notação .md em html

## Autor:

**Nome:** Tomás Barbosa Oliveira

**Id:** a100657

## Trabalho efetuado:

O objetivo do trabalho era criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic Syntax" da [Cheat Sheet](https://www.markdownguide.org/cheat-sheet/).

Apesar de na blackboard apenas constarem alguns elementos dessa _Basic Syntax_, decidi implementar todos os elementos que existiam na mesma, visto que apenas faltavam três elementos para ter todas as funcionalidades básicas completas.

De uma forma geral, foram criadas as conversões de md para html para:
- Heading
- Bold
- Italic
- Blockquote
- Ordered List
- Unordered List
- Code
- Horizontal Rule
- Link
- Image

Todas estas foram feitas recorrendo à biblioteca `re` e utilizando expressões regulares para fazer a procura e substituição dos vários elementos que precisavamos com base na sintaxe.

Em todo o código foi utilizado o método `re.sub` para fazer a substituição dos elementos, e utilizada também a flag `re.MULTILINE` para que certas expressões regulares funcionassem como pretendido.



**Para correr o programa:** 

```python3 script.py inputFile.md```

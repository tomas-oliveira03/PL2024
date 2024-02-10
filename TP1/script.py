import sys
import io

# Para garantir que não existem desformatações de texto
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

modalidades = set()
cont = 0
aptos = 0
idades = {}

for line in sys.stdin:
    if cont != 0:
        colunas = line.split(",")
        modalidade = colunas[8]
        apto = colunas[12]
        idade = int(colunas[5])

        modalidades.add(modalidade)

        if idade in idades:
            current_idade = idades[idade]
            idades[idade] = current_idade + 1
        else:
            idades[idade] = 1

        if apto == "true\n":
            aptos += 1

    cont += 1

cont -= 1

modalidades = sorted(modalidades)
print(f"Modalidades: {modalidades}")
print("------------------")
print(f"Atletas aptos: {'{:.2f}'.format((aptos/cont)*100)}%")
print(f"Atletas inaptos: {'{:.2f}'.format(((cont-aptos)/cont)*100)}%")
print("------------------")
print("Escalões: ")

idade_maxima = max(idades)
for i in range(0, idade_maxima+1, 5):
    atletas_escalao = 0
    for f in range(i, i+5):
        atletas_escalao += idades.get(f, 0)
    if atletas_escalao > 0:
        print(f"   [{i}-{i+4}]: {atletas_escalao}")


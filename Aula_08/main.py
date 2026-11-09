with open('./notas_alunos.txt', "r", encoding="utf-8") as file:
    linhas = file.readlines()

for linha in linhas:
    print(linha.strip())

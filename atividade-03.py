import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
idades = []
alturas = []
pesos = []
imc = []

# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    # Verificando se o usuário quer sair
    if nome.lower() == 'sair':
        break
    
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    
    # Adicionando os dados às listas
    nomes.append(nome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)

# Função para calcular e mostrar classificação
def calcular_imc (pesos, alturas):
    return peso / (altura ** 2)

def classificar_imc (imc):
    if imc < 18.5:
        "abaixo do peso"
    elif 18.5 <= 25:
        "peso normal"
    elif 25 <= imc < 30:
        "sobrepeso"    
    elif 30 <= imc < 35:
        "obesidade grau I"
    elif 35 <= imc < 40:
        "obesidade grau II"
    elif imc >= 40:
         "obesidade grau III"
    return classificar_imc
    
# Exemplos de uso:
peso = float(input("Digite seu peso em quilogramas: "))
altura = float(input("Digite sua altura em metros: "))

imc = calcular_imc(peso, altura)

# Exibindo os dados armazenados
logoSenai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    print(f"Usuário {i+1}:")
    print("Nome:", nomes[i])
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")
    print(f"seu imc é : {imc: .2f}")
    print(f"classificação: {classificar_imc}")
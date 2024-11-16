#Author: Kerllon Rodrigues
#Data: Novembro 2024
#Projeto 03

# Definir peso e altura
peso = int(input('Insira o seu peso (em kg): '))
altura = float(input('Insira a sua altura (em metros): '))

# Calcular o IMC
imc = peso / altura**2

# Exibir o IMC
print(f'O seu IMC é: {imc:.2f}')

# Classificar o IMC
if imc < 18.5:
    print('Seu IMC está: Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Seu IMC está: Normal')
elif 25 <= imc < 30:
    print('Seu IMC está: Sobrepeso')
else:
    print('Seu IMC está: Obesidade')


# aula 5 de Python Turma 21 - 29/11/2023
# programa para converter graus celsius em fahrenheit

# importando funções de outro arquivo
from funcoesConversorTemperatura import celsius_para_fahrenheit, fahrenheit_para_celsius

# Apresentação
print('\n\t\t\t -- Conversor de Temperatura --\n')

print("Digite o número da opção desejada")
print("1. Converter Celsius para Fahrenheit")
print("2. Converter Fahrenheit para Celsius")

opcao = input("Digite a opção: ")

if opcao == "1":
        celsius = float(input("\nDigite a temperatura em Celsius: "))
        resultado = celsius_para_fahrenheit(celsius)
        print(f"{celsius}°C equivale a {resultado:.2f}°F\n")

elif opcao == "2":
        fahrenheit = float(input("\nDigite a temperatura em Fahrenheit: "))
        resultado = fahrenheit_para_celsius(fahrenheit)
        print(f"{fahrenheit}°F equivale a {resultado:.2f}°C\n")
else:
    print("Opção inválida. Por favor, digite 1 ou 2 para uma das opções disponíveis.\n")

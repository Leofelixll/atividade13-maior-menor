# Exercício Python 13: Faça um programa que leia três números e
# mostre qual é o maior e qual é o menor.

numero1 = int(input("digite o primeiro numero: "))
numero2 = int(input("digite o segundo numero: "))
numero3 = int(input("digite o terseiro numero: "))

maior = numero1

if numero1 > numero2 and numero3:
    print("O número um é o maior: ", numero1)
elif numero2 > numero1 and numero3:
    print("O número dois é o maior: ", numero2)
elif numero3 > numero1 and numero2:
    print("O número três é o maior: ", numero3)

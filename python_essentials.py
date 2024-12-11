# -*- coding: utf-8 -*-
"""Python Essentials.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fkqF4LPWAC3DNLEXn8tRx-yW3Es_E8bq
"""

print("Olá, meu nome é João Lucas.")

#Exemplo 2 - Programa para calcular média de altura # Título do programa
# Este programa calcula a média de altura de cinco pessoas.

print("Esse programa irá calcular a média de altura de 5 pessoas")  # Exibe uma mensagem informando o propósito do programa.

altura_1 = float(input("Digite a altura da primeira pessoa"))  # Solicita ao usuário a altura da primeira pessoa e converte para float.
altura_2 = float(input("Digite a altura da segunda pessoa"))  # Solicita ao usuário a altura da segunda pessoa e converte para float.
altura_3 = float(input("Digite a altura da terceira pessoa"))  # Solicita ao usuário a altura da terceira pessoa e converte para float.
altura_4 = float(input("Digite a altura da quarta pessoa"))  # Solicita ao usuário a altura da quarta pessoa e converte para float.
altura_5 = float(input("Digite a altura da quinta pessoa"))  # Solicita ao usuário a altura da quinta pessoa e converte para float.

media_altura = (altura_1 + altura_2 + altura_3 + altura_4 + altura_5) / 5  # Calcula a média das alturas.

print("A média de altura é: ", media_altura)  # Exibe a média calculada.

#Exemplo 3 - Programa para importar biblioteca math

import math

print("A raiz quadrada de 9 é: ", math.sqrt(9))

print("A área da circunferência de raio 2 é: ", math.pi * math.pow(2, 2))

print("A área da circunferência de raio 2 é: ", math.pi * (2)**2)

#2.1.5   LAB   Working with the print() function

print("Hello, Python!")

print("Guilherme")

print("Gandalf")
print("Led Zeppelin")


#2.1.8

print("The itsy bitsy spider\nclimbed up the waterspout.")
print()
print("Down came the rain\nand washed the spider out.")


#2.1.9

print("The itsy bitsy spider" , "climbed up" , "the waterspout.")


#2.1.11

print("My name is", "Python.", end=" ")
print("Monty Python.")

# 2.1.12

print("My", "name", "is", "Monty", "Python.", sep="-")

# 2.1.12

print("My", "name", "is", "Monty", "Python.", sep="?")

# 2.1.12   LAB   The print() function and its arguments

print("Programming","Essentials","in")
print("Python")

print("Programming","Essentials","in", sep="***", end="...")
print("Python")

print("&", "peixe", "salgadinhos", sep=", ")

print('Greg\'s book.')
print("'Greg's book.'")
print('"Greg\'s book."')
print("Greg\'s book.")
print('"Greg's book."')

#2.2.6   LAB   Literais Python - strings

print("\"Eu sou\"\n\"\"aprendizado\"\"\n\"\"\"Python\"\"\"")
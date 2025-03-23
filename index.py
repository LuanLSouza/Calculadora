#Calculadora simples

primeiro_numero = input ("Digite um número: ")

while not primeiro_numero.isnumeric() :
    print("Você não digitou um número válido!")
    primeiro_numero = input ("Digite um número: ")

operadores_validos = ["+", "-", "*", "/"] 

operadores = input ("Digite um operador aritmético: ")

while not operador in operadores_validos :
    print("Você não digitou um operador aritmético válido!")
    operador = input ("Digite um operador aritmético: ")

segundo_numero = input ("Digite um número: ")

while not segundo_numero.isnumeric() :
    print("Você não digitou um número válido!")
    segundo_numero = input ("Digite um número: ")

primeiro_numero = int(primeiro_numero)
segundo_numero = int(segundo_numero)

if operador == "+":
    resultado = primeiro_numero + segundo_numero
if operador == "-":
    resultado = primeiro_numero - segundo_numero
if operador == "*":
    resultado = primeiro_numero * segundo_numero
if operador == "/":
    resultado = primeiro_numero / segundo_numero

linha_resultado = f"{primeiro_numero} {operador} {segundo_numero} = {resultado}"
print(linha_resultado)

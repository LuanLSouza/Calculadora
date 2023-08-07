#Calculadora simples

primeiro_numero = input ("Digite um número ")
while not primeiro_numero.isnumeric() :
    print("Você não digitou um número válido!")
    primeiro_numero = input ("Digite um número ")
operador = input ("Digite um operador aritmético ")
segundo_numero = input ("Digite um número ")
while not segundo_numero.isnumeric() :
    print("Você não digitou um número válido!")
    segundo_numero = input ("Digite um número ")
resultado = ...

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

#digitar os numeros e operação em janela
#tratar os imputs do usuário
#ver números absolutos

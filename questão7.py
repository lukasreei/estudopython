contador = 0
valor = 0

while contador < 5:
    valor = valor + int(input("digite um valor: "))
    contador += 1
print(valor)

media = valor/5
print("a media dos valores é: ", media)
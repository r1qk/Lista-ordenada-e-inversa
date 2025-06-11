import random

print("Exercício")

n = int(input("Digite quantos números terá a lista: "))
lista = []

for i in range(n):
    numero = random.randint(1,50) #int(input("Digite o número:  "))
    lista.append(numero)
    
lista.sort()    
print(lista)

d = len(lista) #dimensão(tamanho de números)
cont = 1 #contador
qtd_trocas = d // 2
for i in range(qtd_trocas):
    t = lista[i]
    lista[i] = lista[d - cont]
    lista[d - cont] = t
    cont += 1
print(lista)

n2 = int(input("Digite quantos números terá a 2° lista: "))
lista2 = []

for i in range(n2):
    numero2 = random.randint(1, 50)
    lista2.append(numero2)

lista2.sort()
print(lista2)

d2 = len(lista2) #dimensão(tamanho de números)
cont2 = 1 #contador
qtd_trocas2 = d2 // 2
for i in range(qtd_trocas2):
    t2 = lista2[i]
    lista2[i] = lista2[d2 - cont2]
    lista2[d2 - cont2] = t2
    cont2 += 1
print(lista2)


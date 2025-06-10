import random

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
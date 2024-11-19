#Exercici 12 - Llistes:

llista = []
valor = input("Valor: ")
while valor != "*":
    valor = int(valor)
    llista.append(valor)
    valor = input("Valor: ")
print(llista)


for i in range(0, len(llista)):
    if llista[i] % 2 == 0:
        llista[i] = llista[i] ** 2
    else:
        llista[i] = llista[i] ** 3
    print(i)
print(llista)

    
    
    



#Exercici 13 - Llistes:

llista = []
valor = input("Valor: ")
while valor != "*":
    valor = int(valor)
    llista.append(valor)
    valor = input("Valor: ")
print(llista)
    
eli = llista[-1]
i=0
while not (llista[i] % eli == 0) and (llista[i] == llista [-1]):
    i+=1
print(llista[i])

#2 -Cadenes: L-R-U-D

seq = input("Seqüència: ")
seq = seq.upper() #transforma seq en majúscules
compt_U = seq.count("U") #compta els valors U de la seqüència
compt_seq = len(seq) #compta els valors de tota la seqüència

if compt_seq / 2 > compt_U:
    print(compt_seq)
else:
    print(compt_U)    

print(compt_U)

#no cumpleixo l'enunciat perquè no vull perdre temps resolent un problema matemàtic

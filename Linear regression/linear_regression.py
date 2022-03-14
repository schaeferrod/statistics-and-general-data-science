tensao = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
corrente = [0, 2.35*10**-3, 5.8*10**-3, 7.2*10**-3, 11.4*10**-3, 13.2*10**-3, 16.2*10**-3, 17.9*10**-3, 22*10**-3, 23.5*10**-3, 25.5*10**-3]

tamanho_listas = len(tensao) == len(corrente)
print(f"Tamanho da lista de tensão e corrente é igual?")

if tamanho_listas == True:
    print("Verdadeiro")
else:
    print("Falso, cheque se a relação de pontos de corrente e tensão é igual!")

n = len(tensao) or len(corrente) #número de componentes




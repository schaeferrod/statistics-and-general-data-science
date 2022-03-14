tensao = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
corrente = [0, 2.35*10**-3, 5.8*10**-3, 7.2*10**-3, 11.4*10**-3, 13.2*10**-3, 16.2*10**-3, 17.9*10**-3, 22*10**-3, 23.5*10**-3, 25.5*10**-3]

tamanho_listas = len(tensao) == len(corrente)
print(f"Tamanho da lista de tensão e corrente é igual?")

if tamanho_listas == True:
    print("Verdadeiro")
else:
    print("Falso, cheque se a relação de pontos de corrente e tensão é igual!")

n = len(tensao) or len(corrente) #número de componentes

soma_corrente = 0
for i in corrente: #Faz o somatório das correntes da lista corrente
    soma_corrente = i + soma_corrente

soma_tensao = 0
for v in tensao: #Faz o somatório das tensões da lista tensao
    soma_tensao = v + soma_tensao

soma_corrente_quadrado = soma_corrente**2 #Faz a potenciação
#ao quadrado do somatório das correntes

soma_corrente_quadratico = 0
for i in corrente:#somatório do quadrado das correntes
    soma_corrente_quadratico = i**2 + soma_corrente

for c in corrente:
    for t in tensao:
        xy = corrente*tensao
        print(xy)




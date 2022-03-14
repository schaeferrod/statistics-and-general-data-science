tensao = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
corrente = [0, 2.35, 5.8, 7.2, 11.4, 13.2, 16.2, 17.9, 22, 23.5, 25.5]

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

indice = 0
lista_corrente_tensao = []
for c in corrente:
    produto_corrente_tensao = corrente[indice]*tensao[indice]
    lista_corrente_tensao.append(produto_corrente_tensao) #add o produto a lista criada

    
    indice = indice + 1
print(lista_corrente_tensao)

somatorio_produto_corrente_tensao = 0
for p in lista_corrente_tensao:
    somatorio_produto_corrente_tensao =  p + somatorio_produto_corrente_tensao
print(somatorio_produto_corrente_tensao)

#Cálculo de B

B = ((n*somatorio_produto_corrente_tensao)-(soma_corrente*soma_tensao))/(n*soma_corrente_quadratico-soma_corrente_quadrado)

print(B)




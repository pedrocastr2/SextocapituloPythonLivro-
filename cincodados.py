import random 

#loop de jogo

continuar = True
while continuar:
    #joga os cinco dados
    dados= [0,0,0,0,0]
    for i in range(5): #escolher um número de 1 a 6
        dados[i] = random.randint(1,6)
    print("A rolagem de seus dados : ", dados) #Exibe os valores dos dados
    
    #Ordena os dados
    dados.sort()
    
    #verifica se há cinco dados iguais
    if dados[0] == dados[4]:
        print("Penta, um Yahtzee!")
        
    #Quadra , verifica seus os quatros primeiros e os quatros últimos são iguais
    elif (dados[0] == dados[3]) or (dados[1] == dados[4]):
        print("Quadra, quatro para o rei")
        
        
         
    #Quadra , verifica seus os quatros primeiros e os quatros últimos são iguais
    elif (dados[0] == dados[3]) or (dados[1] == dados[4]):
        print("Quadra, quatro para o rei")
        
    continuar = (input("Digite [Enter] to keppe going(continuar) , digite qualquer tecla para sair: ")   == '')
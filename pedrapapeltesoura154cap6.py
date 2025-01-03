import random 
choices = ["pedra" , "papel" , "tesoura"]

print("------------------------------------------------------------------")
print("Pedra esmaga tesoura , papel embulha pedra e tesoura corta papel")

player = input("Qual você vai escolher pedra , papel ou tesoura ( ou sair)")
               
while  player != "sair": # Continua jogando até o jogador escolher parar
    player = player.lower()
    
    
    computador = random.choice(choices) # computador escolhe um item
    print ("Sua escolha " +player+ " vs escolha do computador " + computador)
    
    if player == computador:
        print("------------------------------------------------------------------")
        print("Embate")
        print("------------------------------------------------------------------")
        
    elif player == "pedra":
       if computador =="tesoura":
         print("------------------------------------------------------------------")
         print("Vitória")
         print("------------------------------------------------------------------")  
       else:
         print("------------------------------------------------------------------")
         print("Derrota")
         print("------------------------------------------------------------------")     
       
    elif player == "papel":
       if computador =="pedra":
         print("------------------------------------------------------------------")
         print("Vitória")
         print("------------------------------------------------------------------")  
       else:
         print("------------------------------------------------------------------")
         print("Derrota")
         print("------------------------------------------------------------------")  
    
    
    elif player == "tesoura":
       if computador =="papel":
         print("------------------------------------------------------------------")
         print("Vitória")
         print("------------------------------------------------------------------")  
       else:
         print("------------------------------------------------------------------")
         print("Derrota")
         print("------------------------------------------------------------------")  
    
    
    else:
        print("Acho que occoreu um ero")
    print()
    player = input("Quer escolher pedra, papel e tesoura (ou sair)" )
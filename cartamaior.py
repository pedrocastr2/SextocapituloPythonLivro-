import random
napies = ["copas","ouros","paus","espadas"]
numero = ["dois","tres","quatro","cinco","seis","sete","oito","nove","dez","bispo","rainha","rei","as"]

keep_going = True
while  keep_going:
    meu_napies = random.choice(napies) 
    meu_numero  = random.choice(numero) 
    seu_napies  = random.choice(napies) 
    seu_numero  = random.choice(numero) 

    print("Eu tenho uma carta",meu_numero, 'de',meu_napies)
    print("Você tem uma carta",seu_numero, 'de',seu_napies)
    if numero.index(meu_numero) > numero.index(seu_numero):
        print("Eu ganhei")
    elif numero.index(meu_numero) < numero.index(seu_numero):    
        print("Você ganhou")
    else:
        print("Embate")
    answer = input("Digite [Enter] to keppe going(continuar) , digite qualquer tecla para sair: ")
    keep_going = (answer == "")
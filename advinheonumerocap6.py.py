import random

numero = random.randint(1,10)

advinhar = int(input("Advinhe o número: "))

while advinhar != numero:
     if advinhar > numero:
         print(advinhar,"Chutou muito alto, tente novamente")
     if advinhar < numero:
          print(advinhar,"Chutou muito baixo, tente novamente")
     advinhar = int(input("Tente denovo: "))
print("Acertou o número , Parabéns!!!!")
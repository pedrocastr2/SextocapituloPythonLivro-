import random
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors=["red","gray","green","yellow","blue","orange","white","purple","pink"]

for n in range(50):
    #código que gera espirais de cores e tamanhos aleatórios em posições aleatórias
    t.pencolor(random.choice(colors)) #Escolhe uma cor aleatória
    size = random.randint(10,40)   #Escolhe um um tamanho aleatório para a espiral
    
    #Gera uma posição (x,y) aleatória na tela
    
    x = random.randrange(-turtle.window_width()//2  , turtle.window_width()//2)
    y = random.randrange(-turtle.window_height()//2  , turtle.window_height()//2)
    
    
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(91)
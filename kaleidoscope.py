import random 
import turtle
t= turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red","blue","yellow","green","purple" ,"orange","white","gray"]

for n in range(50):
    #gera espirais de cores e tamanhos aleatórios em posições aleatórias na tela
    t.pencolor(random.choice(colors)) #escolhe uma cor aleatória
    size = random.randint(10,40)

    #gera a posição (x,y) aleatória na tela
    x= random.randrange(0,turtle.window_width()//2)
    y= random.randrange(0,turtle.window_height()//2)
    
    #primeira espiral
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(91)
        
    #segunda espiral
    t.penup()
    t.setpos(-x,y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(91)
        
    #primeira espiral
    t.penup()
    t.setpos(x,-y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(91)
        
    #primeira espiral
    t.penup()
    t.setpos(-x,-y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(91)
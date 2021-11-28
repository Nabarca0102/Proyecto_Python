#!/usr/bin/python3

# Curso: Programación bajo plataformas abiertas
# Estudinates:
# Juarez Moraga Adonay B74047
# Abarca Obregón Nelber
# Prado Francklin

'''
Este programa es la elaboración del juego Snake
'''


# Se importan librerias
import turtle
import time
import random

atrasar = 0.1

# Se configura la ventana
# Se declara variable ventana.
# Se configura para que muestre color, titulo y demas. 
ventana = turtle.Screen()
ventana.title('Juego de snake')
ventana.bgcolor('green')
ventana.setup(width= 600, height=600)
ventana.tracer(0)


# Se configura la cabeza de la serpiente.
# Se añade color, direcion y demas. 
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape('square')
cabeza.color('black')
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = 'stop'


# Definir los metodos de comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape('circle')
comida.color('red')
comida.penup()
comida.goto(0,0)
comida.direction = 'stop'


# Funcion para las teclas.
def izquierda():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right"
def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"


# Se define funciones de movimiento
def movimiento():
    if cabeza.direction == "up":
        # Cordenada y
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    if cabeza.direction == "down":
        # Cordenada y
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    if cabeza.direction == 'left':
        # Cordenada x
        x = cabeza.xcor()
        cabeza.setx(x - 20)
    if cabeza.direction == 'right':
        # Cordenada y
        x = cabeza.xcor()
        cabeza.setx(x + 20)

# Se crea funcion que vincula con las teclas.
ventana.listen()
ventana.onkeypress(arriba, "Up")
ventana.onkeypress(abajo, "Down")
ventana.onkeypress(izquierda, "Left")
ventana.onkeypress(derecha, "Right")

# Se crea una lista nueva
# Se agrega segmentación a la serpiente.
lista = []

while True:
    ventana.update()
    # Coliciones con la pared
    if cabeza.xcor() > 280:
        cabeza.goto(-300,0)



    # Coliciones con la comida 
    if cabeza.distance(comida) < 20:
        cor_x = random.randint(-280,280)
        cor_y = random.randint(-280,280)
        comida.goto(cor_x, cor_y)

        siguinte_cabe = turtle.Turtle()
        siguinte_cabe.speed(0)
        siguinte_cabe.shape('square')
        siguinte_cabe.color('grey')
        siguinte_cabe.penup()
        lista.append(siguinte_cabe)
    
    # Se asigana siguiente_cabe para extender cabeza
    serpiente_total = len(lista)

    # Se intera los bloques nuevos
    for i in range(serpiente_total-1, 0, -1):
        cor_x = lista[i - 1].xcor()
        cor_y = lista[i - 1].ycor()
        lista[i].goto(cor_x, cor_y)

    # Se implememta condicional para añadir segmentos
    if serpiente_total > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        lista[0].goto(x, y)

 


        


    movimiento()
    time.sleep(atrasar)

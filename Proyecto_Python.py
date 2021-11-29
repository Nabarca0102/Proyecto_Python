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
lista = []
#Variables de conteo puntos
score = 0
high_score = 0
serpiente_total = len(lista)
        

# Se configura la ventana
# Se declara variable ventana.
# Se configura para que muestre color, titulo y demas. 
ventana = turtle.Screen()
ventana.title('Adonay se la come entera')
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
#comida.direction = 'stop'

#segmentos = []



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


# Metodos imprimir texto en pantalla
texto = turtle.Turtle()
texto.speed(0)
texto.color("black")
texto.penup()
texto.hideturtle()
texto.goto(-280, 270)
#texto.write("PUNTOS: 0  RECORD: 0".format(PUNTOS, RECORD), 
#            font =("Courier", 16, "normal"))



while True:
    ventana.update()
    # Coliciones con las paredes
    if cabeza.xcor() > 300:
        cabeza.goto(-300, y)
    
    elif cabeza.xcor() < -300:
        cabeza.goto(300, y)
        
    elif cabeza.ycor() > 300:
        cabeza.goto(x, -300)
    
    elif cabeza.ycor() < -300:
        cabeza.goto(x, 300)
    
    

    # Coliciones con la comida 
    if cabeza.distance(comida) < 20:
        cor_x = random.randint(-280,280)
        cor_y = random.randint(-280,280)
        comida.goto(cor_x, cor_y)

        #nuevo segmento tras comer
        siguinte_cabe = turtle.Turtle()
        siguinte_cabe.speed(0)
        siguinte_cabe.shape('square')
        siguinte_cabe.color('grey')
        siguinte_cabe.penup()
        lista.append(siguinte_cabe)
        
        
        #Contador de puntos
        score += 10
        if score > high_score:
            high_score = score
            
        texto.clear()
        texto.write("Puntos: {}  Record: {}".format(score, high_score), 
                    font=("Courier", 16))
        
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
    
    #Colisiones con el cuerpo
    for segmento in lista:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"
            
            #Escondemos segmentos
            for segmento in lista:
                segmento.goto(1000, 1000)
            lista.clear
               
            # Reinicio del marcador
            score = 0
            texto.clear()
            texto.write("Puntos: {}  Record: {}".format(score, high_score), 
                        font=("Courier", 16))
    
    time.sleep(atrasar)
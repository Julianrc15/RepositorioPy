import math
import pygame
import random
from pygame import mixer

# inicializar pygame
pygame.init()

# crear Pantalla
pantalla= pygame.display.set_mode((800,600))

#Titulo e Icono
pygame.display.set_caption("Space invaders")
icono= pygame.image.load("Proyectos_PY\JuegoSpaceX\spaceship.png")
pygame.display.set_icon(icono)
fondo= pygame.image.load("Proyectos_PY\JuegoSpaceX\pantalla.png")

#musica de fondo
mixer.music.load("Proyectos_PY\JuegoSpaceX\MusicaFondo.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)

#jugador
img_jugador=pygame.image.load("Proyectos_PY\JuegoSpaceX\spaceship1.png")
jugador_x=368
jugador_y=500
jugador_x_cambio=0

#enemigo
img_enemigo=[]
enemigo_x=[]
enemigo_y=[]
enemigo_x_cambio= []
enemigo_y_cambio= []
cantidad_enemigos= 8

for e in range(cantidad_enemigos):

    img_enemigo.append(pygame.image.load("Proyectos_PY\JuegoSpaceX\enemigo.png"))
    enemigo_x.append(random.randint(0,736))
    enemigo_y.append(random.randint(50,200))
    enemigo_x_cambio.append( 0.4 )
    enemigo_y_cambio.append( 50 )

#bala
img_bala=pygame.image.load("Proyectos_PY\JuegoSpaceX\lasser.png")
bala_x=0
bala_y=500
bala_x_cambio= 0
bala_y_cambio= 1.5
bala_visible= False

#puntaje
puntaje=0
fuente= pygame.font.Font('freesansbold.ttf', 32)
texto_x= 10
texto_y = 10

#función mostrar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Score: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto,(x,y))




#función jugador
def jugador(x,y):
    pantalla.blit(img_jugador, (x,y))


#función enemigo
def enemigo(x,y, enemigo):
    pantalla.blit(img_enemigo[e], (x,y))

#función disparar_bala
def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))

def hay_colision(x1,y1, x2,y2):
    distancia=math.sqrt(math.pow(x1-x2,2)+ math.pow(y2-y1,2))
    if distancia < 27:
        return True
    else:
        return False




# loop del juego
se_ejecuta=True

    
while se_ejecuta:

    #rgb
    # pantalla.fill((205,144,228))
    pantalla.blit(fondo,(0,0))
   
   
    #evento cerrar
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        
        #presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -1
                print("izq")
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 1
                print("der")
            if evento.key == pygame.K_SPACE:
                sonido_bala= mixer.Sound("Proyectos_PY\JuegoSpaceX\disparo.mp3")

                if not bala_visible:
                    sonido_bala.play()
                    bala_x= jugador_x
                    disparar_bala(bala_x,bala_y)
                       
        #soltar teclas            
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0
                print("solto")
                
              



    #modificar posicion Jugador
    jugador_x += jugador_x_cambio
    # jugador_y += jugador_yCambio

    #mantener dentro de lo bordes al jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x=736

        
    #modificar enemigo
    for e in range(cantidad_enemigos):
        enemigo_x[e] += enemigo_x_cambio[e]
   
    #mantener dentro de lo bordes al enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.4
            enemigo_y [e]+= enemigo_y_cambio[e]
        elif enemigo_x [e]>= 736:
            enemigo_x_cambio[e]= -0.4
            enemigo_y[e]+= enemigo_y_cambio[e]

        #colision
        colision =(hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y))
        if colision:
            sonido_colision= mixer.Sound("Proyectos_PY\JuegoSpaceX\Golpe.mp3")
            sonido_colision.play()
            bala_y= 500
            bala_visible= False
            puntaje += 1
            enemigo_x[e]=random.randint(0,736)
            enemigo_y[e]=random.randint(50,200)
            
        enemigo(enemigo_x[e],  enemigo_y[e], e)


    #movimiento bala
    if bala_y <= -32:
        bala_y = 500
        bala_visible = False

    if bala_visible:
        disparar_bala( bala_x, bala_y )
        bala_y -= bala_y_cambio 

    


    jugador(jugador_x,jugador_y)

    mostrar_puntaje(texto_x,texto_y)
    


    #actualizar
    pygame.display.update()

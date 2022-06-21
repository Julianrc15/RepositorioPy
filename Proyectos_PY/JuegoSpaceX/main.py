import pygame
import random

# inicializar pygame
pygame.init()

# crear Pantalla
pantalla= pygame.display.set_mode((800,600))

#Titulo e Icono
pygame.display.set_caption("Space invaders")
icono= pygame.image.load("Proyectos_PY\JuegoSpaceX\spaceship.png")
pygame.display.set_icon(icono)
fondo= pygame.image.load("Proyectos_PY\JuegoSpaceX\pantalla.png")

#jugador
img_jugador=pygame.image.load("Proyectos_PY\JuegoSpaceX\spaceship1.png")
jugador_x=368
jugador_y=500
jugador_x_cambio=0

#enemigo
img_enemigo=pygame.image.load("Proyectos_PY\JuegoSpaceX\enemigo.png")
enemigo_x=random.randint(0,736)
enemigo_y=random.randint(50,200)
enemigo_x_cambio= 0.1
enemigo_y_cambio= 50

#bala
img_bala=pygame.image.load("Proyectos_PY\JuegoSpaceX\lasser.png")
bala_x=0
bala_y=500
bala_x_cambio= 0
bala_y_cambio= 0.7
bala_visible= False




#función jugador
def jugador(x,y):
    pantalla.blit(img_jugador, (x,y))


#función enemigo
def enemigo(x,y):
    pantalla.blit(img_enemigo, (x,y))

#función disparar_bala
def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))




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
                jugador_x_cambio = -0.5
                print("izq")
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.5
                print("der")
            if evento.key == pygame.K_SPACE:
                if not bala_visible:
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
    enemigo_x += enemigo_x_cambio
   
    #mantener dentro de lo bordes al enemigo
    if enemigo_x <= 0:
        enemigo_x_cambio = 0.1
        enemigo_y += enemigo_y_cambio
    elif enemigo_x >= 736:
        enemigo_x_cambio= -0.1
        enemigo_y += enemigo_y_cambio

    #movimiento bala
    if bala_y <= -32:
        bala_y = 500
        bala_visible = False

    if bala_visible:
        disparar_bala( bala_x, bala_y )
        bala_y -= bala_y_cambio 


    jugador(jugador_x,jugador_y)
    enemigo(enemigo_x,  enemigo_y)
    #actualizar
    pygame.display.update()

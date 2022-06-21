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

#jugador
img_jugador=pygame.image.load("Proyectos_PY\JuegoSpaceX\spaceship1.png")
jugador_x=368
jugador_y=536
jugador_x_cambio=0

#enemigo
img_enemigo=pygame.image.load("Proyectos_PY\JuegoSpaceX\enemigo.png")
enemigo_x=random.randint(0,736)
enemigo_y=random.randint(50,200)
enemigo_x_cambio= 0.1
enemigo_y_cambio= 50


#función jugador
def jugador(x,y):
    pantalla.blit(img_jugador, (x,y))


#función enemigo
def enemigo(x,y):
    pantalla.blit(img_enemigo, (x,y))





# loop del juego
se_ejecuta=True

    
while se_ejecuta:

    #rgb
    pantalla.fill((205,144,228))
   
   
    #evento cerrar
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        
        #presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.1
                print("izq")
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.1
                print("der")
                       
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
    elif enemigo_x >= 736:
        enemigo_x_cambio= -0.1


    jugador(jugador_x,jugador_y)
    enemigo(enemigo_x,  enemigo_y)
    #actualizar
    pygame.display.update()

from figura_class import Pelota, Raqueta
import pygame as pg

pg.init()

pantalla_principal = pg.display.set_mode((800,600))
pg.display.set_caption("Pong")

#definir la tasa de refresco de nuestro bucle de fotogramas fps
cronometro = pg.time.Clock()

pelota = Pelota(400,300)
raqueta1 = Raqueta(20,300) 
raqueta2 = Raqueta(780,300)

game_over = False

while not game_over:
    #imprimir los milisegundos que tarda cada fotograma actualmente
    vt = cronometro.tick(300)#int variable para controlar la velocidad entre fotogramas
    #print(vt)

    for evento in pg.event.get():
        if evento.type == pg.QUIT:
           game_over = True

    #p1 = (400,0)
    #p2 = (400,400)

    pantalla_principal.fill((158, 95, 39))
    pg.draw.line(pantalla_principal,(255,255,255), (400,0), (400,600), width=2)
    #pg.draw.lines(pantalla_principal,(255,255,255), False, (p1, p2), width=2)
    pelota.dibujar(pantalla_principal)
    pelota.mover()
    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)
    raqueta1.mover(pg.K_w, pg.K_s)
    raqueta2.mover(pg.K_UP, pg.K_DOWN)
    pg.display.flip()
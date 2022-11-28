from figura_class import Pelota, Raqueta
import pygame as pg

pg.init()

pantalla_principal = pg.display.set_mode((800,600))
pg.display.set_caption("Pong")

pelota = Pelota(400,300)
raqueta1 = Raqueta(20,300) 
raqueta2 = Raqueta(780,300)

game_over = False

while not game_over:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
           game_over = True

        """""""""
        #mover raqueta
        if evento.type == pg.KEYDOWN:
            if evento.key == pg.K_UP:
                raqueta1.pos_y -= 20
            elif evento.key == pg.K_DOWN:
                raqueta1.pos_y += 20
        """""

        estado_teclas = pg.key.get_pressed()

        if estado_teclas[pg.K_UP] == True:
            raqueta1.pos_y -= 1
        if estado_teclas[pg.K_DOWN] == True:
            raqueta1.pos_y += 1


    pantalla_principal.fill((158, 95, 39))
    pg.draw.line(pantalla_principal,(255,255,255), (400,0), (400,600), width=2)
    pelota.dibujar(pantalla_principal)
    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)
    pg.display.flip()
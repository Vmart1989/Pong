import pygame as pg
from figura_class import Raqueta, Pelota

#por convenio, definir variables en mayuscula significa que es una constante, fija
ANCHO = 800
ALTO = 600
BLANCO = (255,255,255)
TIERRA = (158, 95, 39)
NEGRO = (0, 0, 0)
AMARILLO =(218, 241, 47)
NARANJA = (230, 40, 13)

class Partida:
    def __init__(self):
        pg.init()
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("Pong")
        self.tasa_refresco = pg.time.Clock()
        self.pelota = Pelota(ANCHO//2, ALTO//2,vx=1, vy=1)
        self.raqueta1 = Raqueta(10,ALTO//2,vy=2) 
        self.raqueta2 = Raqueta(ANCHO-10,ALTO//2,vy=2)
        self.font = font = pg.font.Font("fonts/ZenDotsRegular.ttf",15) #None es el estilo de fuente y 30 el tamano
        self.fuenteTemp = pg.font.Font('fonts\ZenDotsRegular.ttf', 20)
        self.marcador1 = 0
        self.marcador2 = 0
        self.quienMarco = ""
        self.temporizador = 11000 #en milisegundos(10 segundos que incia en 15)

    def bucle_fotograma(self):
        game_over = False
        while not game_over and (self.marcador1 < 10 or self.marcador2 < 10) and self.temporizador >0:
            
            salto_tiempo = self.tasa_refresco.tick(280)
            self.temporizador -= salto_tiempo

            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True

            
            self.raqueta1.mover(pg.K_w, pg.K_s)
            self.raqueta2.mover(pg.K_UP, pg.K_DOWN)
            self.quienMarco = self.pelota.mover()
            
            self.pantalla_principal.fill (self.parpadeo())
        
            

            self.pelota.choque(self.raqueta1, self.raqueta2)
            self.marcador()
            self.linea_disc()
            self.pelota.dibujar(self.pantalla_principal)
            self.raqueta1.dibujar(self.pantalla_principal)
            self.raqueta2.dibujar(self.pantalla_principal)
            self.mostrar_jugador()
            tiempo = self.font.render(str(int(self.temporizador/1000)),0,AMARILLO)
            self.pantalla_principal.blit(tiempo,(780,10))
            
            pg.display.flip()

        pg.quit()

    def mostrar_jugador(self):
        jugador1 = self.font.render(str("Jugador 1"), 0, (NEGRO))
        jugador2 = self.font.render(str("Jugador 2"), 0, (NEGRO))
        self.pantalla_principal.blit(jugador1, (160,10))
        self.pantalla_principal.blit(jugador2, (560,10))
    
    def marcador(self):
        marcadorIzq = self.font.render(str(self.marcador1),0, (NEGRO))
        marcadorDer = self.font.render(str(self.marcador2),0, (NEGRO))
        self.pantalla_principal.blit(marcadorDer, (200,30))
        self.pantalla_principal.blit(marcadorIzq, (600,30))

        if self.quienMarco == "right":
            self.marcador2 += 1
        elif self.quienMarco == "left":
            self.marcador1 += 1

    def linea_disc(self):
        cont_linea1=0 #variables para dibujar la linea discontinua
        cont_linea2=50
        while cont_linea1 <= 560 and cont_linea2 <= 630:
            pg.draw.line(self.pantalla_principal,(BLANCO), (400,cont_linea1), (400,cont_linea2), width=10)
            cont_linea1 += 70
            cont_linea2 += 70

    def parpadeo(self):
        if self.temporizador <=5000 and self.temporizador >=4000:
            return NARANJA
        if self.temporizador <=3000 and self.temporizador >=2000:
            return NARANJA
        if self.temporizador <=1000 and self.temporizador >=0:
            return NARANJA
        else:
            return TIERRA

class Menu:
    def __init__(self):
        pg.init()
        self.pantalla_principal = pg.display.set_mode( (ANCHO,ALTO) )
        pg.display.set_caption('Menu')
        self.tasa_refresco = pg.time.Clock()

        self.imagenFondo = pg.image.load('images/fondomenu.jpg')
        self.fuenteMenu = pg.font.Font('fonts/ZenDotsRegular.ttf',20)

    
    def bucle_pantalla(self):
        game_over = False

        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True
            
            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_RETURN:
                    game_over = True
                    return "jugar"

            self.pantalla_principal.blit(self.imagenFondo,(0,0))
            menu = self.fuenteMenu.render("Pulsa ENTER para jugar",0,BLANCO)
            self.pantalla_principal.blit(menu,(240,250))
            pg.display.flip()
        

import pygame as pg
from figura_class import Raqueta, Pelota
from utils import * #traigo las variables del archivo __init__ en utils folder

class Partida:
    def __init__(self, pantalla, refresco): #parametros inicializados en scene_controller.py
        self.pantalla_principal = pantalla
        self.tasa_refresco = refresco
        self.pelota = Pelota(ANCHO//2, ALTO//2,vx=2, vy=2)
        
        self.raqueta1 = Raqueta(10,ALTO//2,vy=2) 
        self.raqueta1.direccion = 'izqda'
        self.raqueta2 = Raqueta(ANCHO-20,ALTO//2,vy=2)
        self.raqueta2.direccion = 'drcha'
        
        self.font = font = pg.font.Font("fonts/PressStart.ttf",10) #None es el estilo de fuente y 30 el tamano
        self.fuenteTemp = pg.font.Font('fonts\PressStart.ttf', 20)
        self.marcador1 = 0
        self.marcador2 = 0
        self.quienMarco = ""
        self.temporizador = TIEMPO_LIMITE #en milisegundos(20 segundos que incia en 15)
        self.sonido = pg.mixer.Sound("sound/pelota.mp3")
        self.sonidopunto = pg.mixer.Sound("sound/point.wav")

    def bucle_pantalla(self):
        #reinicio de estos parametros para volver a jugar:
        self.temporizador = TIEMPO_LIMITE
        self.marcador1 = 0
        self.marcador2 = 0

        game_over = False
        while not game_over and (self.marcador1 < 10 or self.marcador2 < 10) and self.temporizador >0:
            
            salto_tiempo = self.tasa_refresco.tick(280)
            self.temporizador -= salto_tiempo

            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    #game_over = True
                    return True
            
            
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
            tiempo = self.font.render(str(int(self.temporizador/1000)),0,GRIS)
            if self.temporizador <5000:
                tiempo = self.font.render(str(int(self.temporizador/1000)),0,AMARILLO)

            self.pantalla_principal.blit(tiempo,(770,10))
            
            pg.display.flip()            

        return self.resultado_final()
       


    def resultado_final(self):
        if self.marcador1 > self.marcador2:
            return "Gana el Jugador 2, " + str(self.marcador1) + " - " + str(self.marcador2)
        elif self.marcador2 > self.marcador1:
            return "Gana el Jugador 1, " + str(self.marcador2) + " - " + str(self.marcador1)
        else:
            return "Empate, " + str(self.marcador1) +" - " + str(self.marcador2)

    def mostrar_jugador(self):
        jugador1 = self.font.render(str("Jugador 1"), 0, (GRIS))
        jugador2 = self.font.render(str("Jugador 2"), 0, (GRIS))
        self.pantalla_principal.blit(jugador1, (160,10))
        self.pantalla_principal.blit(jugador2, (560,10))
    
    def marcador(self):
        marcadorIzq = self.font.render(str(self.marcador1),0, (GRIS))
        marcadorDer = self.font.render(str(self.marcador2),0, (GRIS))
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
            pg.draw.line(self.pantalla_principal,(GRIS), (400,cont_linea1), (400,cont_linea2), width=10)
            cont_linea1 += 70
            cont_linea2 += 70

    def parpadeo(self):
        if self.temporizador <=5000:
            return NEGRO
        else:
            return GRIS_OSCURO

class Menu:
    def __init__(self, pantalla, refresco):
        self.pantalla_principal = pantalla
        self.tasa_refresco = refresco
        self.imagenFondo = pg.image.load('images/fondomenu.jpg')
        self.fuenteMenu = pg.font.Font('fonts/PressStart.ttf',20)
        self.fuentePong = pg.font.Font('fonts/PressStart.ttf',40)
        self.musica = pg.mixer.Sound("sound/inicio.mp3")
    
    def bucle_pantalla(self):
        
        self.musica.play()

        game_over = False

        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    #game_over = True
                    return True
            
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_RETURN:
                        game_over = True
                        return "jugar"
                    elif evento.key == pg.K_r:
                        game_over = True
                        return "records"


            self.pantalla_principal.blit(self.imagenFondo,(0,0))
            jugar = self.fuenteMenu.render("Pulsa ENTER para jugar",0,GRIS)
            pong = self.fuentePong.render("PONG",0,GRIS)
            record = self.fuenteMenu.render("Pulsa R para ver Records",0,GRIS)
            self.pantalla_principal.blit(jugar,(175,260))
            self.pantalla_principal.blit(pong,(320,100))
            self.pantalla_principal.blit(record,(160,360))
            pg.display.flip()
        self.musica.stop()

class Resultado:
    def __init__(self, pantalla, refresco):
        self.pantalla_principal = pantalla
        self.tasa_refresco = refresco

        self.imagenFondo = pg.image.load('images/fondomenu.jpg')
        self.fuenteResultado = pg.font.Font('fonts/PressStart.ttf',20)
        self.fuenteGameOver = pg.font.Font('fonts/PressStart.ttf',40)
        self.resultado = ""
        #self.sonido = pg.mixer.Sound('sound/resultado.mp3')


    def bucle_pantalla(self):
        game_over = False

        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    #game_over = True
                    return True
            
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_RETURN:
                        game_over = True
                        #return "jugar"
            
            self.pantalla_principal.blit(self.imagenFondo, (0,0))
            gameover = self.fuenteGameOver.render("GAME OVER", 0,GRIS)
            result = self.fuenteResultado.render(self.resultado,0,GRIS)

            self.pantalla_principal.blit(gameover,(220,160))
            self.pantalla_principal.blit(result,(200,250))
            pg.display.flip()
    
    def recibir_resultado(self,resultado):
        self.resultado = resultado
                           
class Records:
    def __init__(self, pantalla, refresco):
        self.pantalla_principal = pantalla
        self.tasa_refresco = refresco
        self.imagenFondo = pg.image.load('images/fondomenu.jpg')
        self.fuenteResultado = pg.font.Font('fonts/PressStart.ttf',20)
        
    def bucle_pantalla(self):
        game_over = False

        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    #game_over = True
                    return True
        
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_RETURN:
                        game_over = True

        self.pantalla_principal.blit(self.imagenFondo, (0,0))
        result = self.fuenteResultado.render("RECORDS",0,GRIS)
        self.pantalla_principal.blit(result,(245,250))
        pg.display.flip()
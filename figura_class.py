import pygame as pg
from utils import GRIS

class Pelota:
    def __init__(self, pos_x,pos_y,radio=12,color=(GRIS), vx=1, vy=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radio = radio
        self.color = color
        self.vx = vx
        self.vy = vy
        self.font = font = pg.font.Font(None,40) #para mostrar marcador

    def dibujar(self,pantalla):
        pg.draw.circle(pantalla,self.color,(self.pos_x, self.pos_y), self.radio)

    def mover(self, y_max=600, x_max=800,y_min=0, x_min=-200):
        self.pos_x += self.vx
        self.pos_y += self.vy

        if self.pos_y >= y_max-self.radio or self.pos_y <0+self.radio:
            self.vy *= -1

        if self.pos_x >= x_max+self.radio*12: 
            self.pos_x = x_max//2
            self.pos_y = y_max//2

            self.vx *= -1
            self.vy *= -1

            return "right"

        if self.pos_x < 0-self.radio*12:
            self.pos_x = x_max//2
            self.pos_y = y_max//2

            self.vx *= -1
            self.vy *= -1

            return "left"
     
    def choque(self,*raquetas): #*funcion epecial *args que recibe multiples parametros
        for r in raquetas:
            if self.derecha >= r.izquierda and\
            self.izquierda <= r.derecha and\
            self.abajo >= r.arriba and\
            self.arriba <= r.abajo:
                self.vx *= -1
                return #return o break se usa para salir del bucle

            
    def marcador(self, pantalla_principal):
        marcadorIzq = self.font.render(str(self.contadorDerecha),0, (0, 0, 0))
        marcadorDer = self.font.render(str(self.contadorIzquierda),0, (0, 0, 0))
        pantalla_principal.blit(marcadorDer, (200,30))
        pantalla_principal.blit(marcadorIzq, (600,30))

    @property #property evita que lo tengas que invocar como una funcion (derecha()), lo hace variable
    def derecha(self):
        return self.pos_x + self.radio
    @property
    def izquierda(self):
        return self.pos_x - self.radio
    @property
    def arriba(self):
        return self.pos_y - self.radio  
    @property
    def abajo(self):
        return self.pos_y + self.radio


class Raqueta:
    def __init__(self, pos_x,pos_y,w=30,h=100,color=(234, 230, 229), vx=1, vy=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.w = w
        self.h = h
        self.color = color
        self.vx = vx
        self.vy = vy

    def dibujar(self,pantalla):
        pg.draw.rect(pantalla,self.color,(self.pos_x-(self.w//2), self.pos_y-(self.h//2), self.w, self.h))

    def mover(self,tecla_arriba,tecla_abajo, y_max=600, y_min=0):
        estado_teclas = pg.key.get_pressed()

        if estado_teclas[tecla_arriba] and self.pos_y > (y_min + self.h//2):
            self.pos_y -= self.vy
        if estado_teclas[tecla_abajo]and self.pos_y < (y_max - self.h//2):
            self.pos_y += self.vy
    
    @property
    def derecha(self):
        return self.pos_x + self.w//2

    @property
    def izquierda(self):
        return self.pos_x - self.w//2
    
    @property
    def arriba(self):
        return self.pos_y - self.h//2  

    @property
    def abajo(self):
        return self.pos_y + self.h//2
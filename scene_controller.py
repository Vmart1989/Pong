from pantallas import *

class SceneController:
    def __init__(self):
       self.menu = Menu()
       self.partida = Partida()
       self.resultado = Resultado()
       self.records = Records()
       self.valor_resultado = ""
       #tarea mejorar codigo de while dentro de start(pista hacerlo con listas)

    def start(self):
        seguir = True

        while seguir:
            
            cerrar = self.menu.bucle_pantalla()
            if cerrar == True:
                break
            
            cerrar = self.valor_resultado = self.partida.bucle_fotograma()
            if cerrar == True:
                break

            self.resultado.recibir_resultado(self.valor_resultado)
            
            cerrar = self.resultado.bucle_resultado()
            if cerrar == True:
                break

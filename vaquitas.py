import os
import random
import time
import threading

inicioPuente = 10
largoPuente = 20

N=1

def ValorarN(tan):
  global N
  N=tan

ValorarN(1)#se tiene que ejecutar antes de definir el semaforo
            #tendria que cambiar ese 2 por algo para escribirlo con teclado en cuanto me entere de como se lo escribiria

VacasPorPuente=threading.Semaphore(N)

class Vaca(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.velocidad = random.uniform(0.1, 0.5)

  global VacasPorPuegitnte

  def avanzar(self):
    if self.posicion == inicioPuente-1:
      VacasPorPuente.acquire()

    if self.posicion == inicioPuente+largoPuente:
      VacasPorPuente.release()

    time.sleep(self.velocidad)
    self.posicion += 1    

  def dibujar(self):
    print(' ' * self.posicion + "V")


  def run(self):
    while(True):
      self.avanzar()


vacas = []
for i in range(5):
  v = Vaca()
  vacas.append(v)
  v.start()

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

def dibujarPuente():
  puente=' ' * inicioPuente + '=' * largoPuente
  print(puente*2)
#el primer puente ya ordena cuantas vacas pueden pasar 
#y llegaran en el mismo orden en el segundo puente 
#por ahora no es nesesario configurar un control de 
#capacidad en el segunfo puente 

while(True):
  cls()
  print('Apreta Ctrl + C varias veces para salir...')
  print()
  dibujarPuente()
  for v in vacas:
    v.dibujar()
  dibujarPuente()

  time.sleep(0.2)
  


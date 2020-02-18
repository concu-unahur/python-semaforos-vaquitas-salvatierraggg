import os
import random
import time
import threading

inicioPuente = 10
largoPuente = 20

VacasPorPuente=threading.Semaphore(2)

class Vaca(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.velocidad = random.uniform(0.1, 0.5)

  global VacasPorPuente

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
  print(' ' * inicioPuente + '=' * largoPuente)

while(True):
  cls()
  print('Apreta Ctrl + C varias veces para salir...')
  print()
  dibujarPuente()
  for v in vacas:
    v.dibujar()
  dibujarPuente()
  time.sleep(0.2)

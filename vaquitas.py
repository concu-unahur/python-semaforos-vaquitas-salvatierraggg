import os
import random
import time
import threading

inicioPuente = 10
largoPuente = 20

pase=threading.Semaphore(1)
avance=threading.Semaphore(largoPuente)


class Vaca(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.velocidad = random.uniform(0.1, 0.5)

  global pase

  def avanzar(self):
    try:
      if self.posicion >= inicioPuente and self.posicion<inicioPuente+largoPuente:
        pase.acquire()
        time.sleep(self.velocidad)
        self.posicion += 1
      
    finally:
        if  self.posicion<inicioPuente:
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

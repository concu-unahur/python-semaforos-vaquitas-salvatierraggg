import os
import random
import time
import threading
N=1

class puente():

  # por defeco cominsan los valores asi
  def __init__(self,inicioPuente,largoPuente):
    self.inicioPuente=inicioPuente
    self.largoPuente=largoPuente

  
Puentes=[]

p = puente(5,10)
Puentes.append(p)
  
p = puente(3,40)
Puentes.append(p)

p = puente(4,16)
Puentes.append(p)


  

def valorarN(tanto):
  global N
  N=tanto

  



valorarN(2)#se tiene que ejecutar antes de definir el semaforo
            #tendria que cambiar ese 2 por algo para escribirlo con teclado en cuanto me entere de como se lo escribiria

VacasPorPuente=threading.Semaphore(N)

class Vaca(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.velocidad = random.uniform(0.1, 0.5)

  global VacasPorPuegitnte

  def avanzar(self):
    if self.posicion == Puentes[0].inicioPuente-1:
      VacasPorPuente.acquire()

    if self.posicion == Puentes[0].inicioPuente+Puentes[0].largoPuente:
      VacasPorPuente.release()

    time.sleep(self.velocidad)
    self.posicion += 1    

  def dibujar(self):
    print(' ' * self.posicion + "V")


  def run(self):
    while(True):
      self.avanzar()
  

def dibujarPuente():
  i=0

  for p in Puentes:
    print(' ' * Puentes[i].inicioPuente + '=' * Puentes[i].largoPuente,end="")
    if i <= len(Puentes):
      i+=1
    else:
      i=0
  print("")
  

vacas = []
for i in range(5):
  v = Vaca()
  vacas.append(v)
  v.start()

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

 

while(True):
  cls()
  print('Apreta Ctrl + C varias veces para salir...')
  print()
  dibujarPuente()
  for v in vacas:
    v.dibujar()
  dibujarPuente()

  time.sleep(0.2)
  


import os
import random
import time
import threading

DistanciaMaxima=1
#link con ayuda para las listas https://uniwebsidad.com/libros/algoritmos-python/capitulo-7/listas

class puente():

  # por defeco cominsan los valores asi
  def __init__(self,inicioPuente,largoPuente,N):
    self.inicioPuente=inicioPuente
    self.largoPuente=largoPuente
    self.VacasPorPuente=threading.Semaphore(N)
    self.tamañoTotal=self.inicioPuente+self.largoPuente
    #memoriaAuxiliar=[]


  
Puentes=[]#3 puentes diferentes con inicio,Largo,y cantidad de 
          #animales que pueden pasar ya que cada puente tiene 
          #su propio semaforo

p = puente(5,10,3)
Puentes.append(p)
  
p = puente(6,4,2)
Puentes.append(p)

p = puente(4,6,1)
Puentes.append(p)

for p in Puentes:
  DistanciaMaxima+=p.tamañoTotal
  #uso una variable para esto por que no se
  #como se escribe para sumar los elementos de la lista

class Vaca(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicionMemoria=0
    self.posicion =0
    self.velocidad = random.uniform(0.1, 0.5) 
    self.pasandoPuente=0
    self.parar=threading.Semaphore()
  

  def avanzar(self):
    global Puentes
    try:
      if self.posicion == Puentes[self.pasandoPuente].inicioPuente+self.posicionMemoria-1:
        Puentes[self.pasandoPuente].VacasPorPuente.acquire()

      if  self.posicion == Puentes[self.pasandoPuente].tamañoTotal+self.posicionMemoria:
        Puentes[self.pasandoPuente].VacasPorPuente.release()
        self.posicionMemoria+=Puentes[self.pasandoPuente].tamañoTotal
        self.pasandoPuente+=1

      time.sleep(self.velocidad)
      self.posicion += 1    
    
    finally:
      if self.posicion>=DistanciaMaxima:  
        self.parar.acquire()

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
  


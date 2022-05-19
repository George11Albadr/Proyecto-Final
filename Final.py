# -*- coding: utf-8 -*-
"""
@author: ge
"""

import requests
import json


class Stack:

  def __init__(self, elementos: list):
    self.elementos = elementos

  def push(self, el):
    self.elementos.append(el)

  def pop(self):
    if(len(self.elementos)>0):
      self.elementos.pop()

  def printValues(self):
    print(self.elementos)

  def getFirst(self):
    return self.elementos[0]  

class Queue:  
  
  def __init__( self, elementos: list):
    self.elementos = elementos

  def add(self, el):
    if(len(self.elementos) == 0):
      self.elementos.append(el)
    else:
      temp = self.elementos.copy()
      temp.reverse()
      temp.append(el)
      temp.reverse()
      self.elementos = temp

  def delete(self):
    if(len(self.elementos)>0):
      self.elementos.pop()

  def getFirst(self):
    return self.elementos[len(self.elementos)-1]     


  def printValues(self):
    print(self.elementos)
      
  
class Tree:
  
  def __init__(self):
    self.val = None
    self.left = None
    self.right = None

  def insert(self, val):
    if self.val:
      if val < self.val:
        if self.left is None:
          self.left = Tree()
          self.left.val = val
        else:
          self.left.insert(val)
      elif val > self.val:
        if self.right is None:
          self.right = Tree()
          self.right.val = val
        else:
          self.right.insert(val)
    else:
      self.val = val

  def printValues(self):
    if self.left:
      self.left.printValues()
      
    print(self.val)
    
    if self.right:
      self.right.printValues()

def ejecutar():
  
  response = requests.get("https://dummyjson.com/products")
  ob = json.loads(response.text)["products"]
  
  puntos = 0

  print("Bienvenido a Guess the price App \n")
  print("-Se le ira mostrando en pantalla una lista de productos de los cuales debera adivinar su rango de precio en dolares \n")
  print("-Dependiendo del modo que escoja la dificultad aumenta asi, cola diferencia de 20 dolares, pila diferencia de 10 dolares, arbol diferencia de 5 dolares  \n")
  print("-El rango se calculara automaticamente, dependiendo del nivel se le sumara la diferencia de rango al precio que usted ingrese y ese sera su rango")
  print("-El intento acaba cuando acabe la lista de productos, al final podra ver su puntaje \n")

  print("1. Modo cola")
  print("2. Modo pila")
  print("3. Modo arbol \n")
  
  modo = int(input("En que modo desea iniciar la app:"))

  precio_diferencia = 20

  estructura = Queue([])

  if(modo == 2):
    estructura = Stack([])
    precio_diferencia = 10
  if(modo == 3):
    estructura = Tree()
    precio_diferencia = 5

  for i in range(0, len(ob)):

    adivino = False
    
    nombre_producto = ob[i]["title"]
    precio_producto = ob[i]["price"]
    
    print("El siguiente producto es: " + nombre_producto)
    
    precio_usuario = float(input("Adivine el precio! : "))

    limite_superior_rango = precio_usuario+precio_diferencia
    
    print("Su rango es $"+ str(precio_usuario)+"-$"+str(limite_superior_rango))
    print("El valor del producto es $"+str(precio_producto))
    if(precio_producto == precio_usuario):
      print("\n ADIVINASTE EL PRECIO! Se agregara el objeto!")
      adivino = True
    elif(precio_producto >= precio_usuario and precio_producto <= limite_superior_rango ):
      print("\n En el rango! Se agregara 1 objeto!")
      adivino = True
    elif(precio_producto < precio_usuario):
      if(modo == 3):
        print("NOO! Pierdes todos los objetos.")
      else:
        print("Noo! Muy por encima! Pierdes 1 objeto")
    else:
      print("Estas por debajo! No pierdes objetos")
      adivino = "Next"

    if(adivino == True):
      if(isinstance(estructura,Queue)):
        estructura.add(nombre_producto)
      elif(isinstance(estructura,Stack)):
        estructura.push(nombre_producto)
      else:
        estructura.insert(nombre_producto)
    elif(adivino == False):
      if(isinstance(estructura,Queue)):
        estructura.delete()
      elif(isinstance(estructura,Stack)):
        estructura.pop()
      else:
        estructura = Tree()
    print("\n Estado de la estructura: ")
    estructura.printValues()

  
  print("\n Tu intento ha acabado, este es tu inventario de objetos: ")  
  estructura.printValues(); 

    
ejecutar()




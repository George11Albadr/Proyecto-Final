# -*- coding: utf-8 -*-
"""
@author: georg
"""
import unittest

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
    return self.elementos[len(self.elementos)-1] 

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


class Test(unittest.TestCase):

  def test_Queue(self):
    cola = Queue([])
    cola.add("Elemento #1")
    cola.add("Elemento #2")
    self.assertEqual(cola.getFirst(),"Elemento #1","Se esperaba elemento")

  def test_Stack(self):
    pila = Stack([])
    pila.push("Elemento #1")
    pila.push("Elemento #2")
    pila.push("Elemento #3")
    pila.pop()
    self.assertEqual(pila.getFirst(),"Elemento #2","Se esperaba elemento")

  def test_tree(self):
    arbol = Tree()
    arbol.val = "Elemento #1"
    arbol.insert("Elemento #2")
    self.assertEquals(arbol.right.val, "Elemento #2")
  
    
unittest.main()


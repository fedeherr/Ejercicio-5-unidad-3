from zope.interface import Interface
from zope.interface import implementer
import numpy as np
class IManejador(Interface):
    def insertarElemento(elemento, pos):
        pass
    def agregarElemento(elemento):
        pass
    def mostrarElemento(pos):
        pass
class Elemento(object):
    __test = 2
    def __init__(self, valor):
        self.__test = valor
    def __str__(self):
        return "Este elemento es de valor %d" % (self.__test)
@implementer(IManejador)
class manejadorElementos():
    __arr = None
    __largo = 0
    def __init__(self, largo = 3):
        self.__largo = largo
        self.__arr = np.empty(self.__largo, dtype = Elemento)
        for i in range(3):
            self.__arr[i] = i+1
    def insertarElemento(self, elemento, pos):
        if (pos > self.__largo-1):
            print ("Error, la posición es mayor a la lista")
        if (pos == self.__largo-1): self.__arr = np.append(self.__arr, elemento)
        if (pos < self.__largo-1):
            auxarr = self.__arr
            auxarr[pos] = elemento
            for i in range(len(self.__arr) - pos - 1):
                auxarr[i + pos] = self.__arr[i + pos]
            auxarr = np.append(auxarr, self.__arr[i + pos])
            self.__largo += 1
            self.__arr = auxarr
        for i in range(len(self.__arr)):
            print(self.__arr)

    def agregarElemento(self, elemento):
        self._arr = np.append(self._arr, elemento)

    def comprobarElemento(self, pos):
        if (pos > self.__largo):
            print ("Error, la posición es mayor a la lista")
            return
        print (self.__arr[pos])

if __name__ == '__main__':
    a = int(input("Ingrese posición a insertar: "))
    c = int(input("Ingrese elemento: "))
    b = manejadorElementos()
    b.insertarElemento(c, a)
    a = int(input("Ingrese posición a comprobar: "))
    b.comprobarElemento(a)


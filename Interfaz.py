from zope.interface import Interface
from zope.interface import implementer
class IManejador(Interface):
    def insertarElemento(elemento, pos):
        pass
    def agregarElemento(elemento):
        pass
    def mostrarElemento(pos):
        pass

from usuario import Usuario
from quarto import Quarto

class Hotel:
    def __init__(self):
      self.clientes = []
      self.quartos = []
      self.reservas = []


    def adicionar(self):
       self.clientes.append(Usuario)

    def addQuarto(self):
       self.quartos.append(Quarto)
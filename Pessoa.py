from Endereco import *
class Pessoa:
  def __init__(self):
    self.__nome=input('Digite seu nome: ' )
    self.__numero=input('Digite seu numero: ')
    self.__endereco=Endereco()
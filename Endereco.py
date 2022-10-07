class Endereco:
  def __init__(self):
    self.__logradouro=input('insira sua rua/avenida: ')
    self.__cidade=input('insira sua cidade: ')
    self.__estado=input('insira seu estado: ')
    def consultarlogradouro(self):
      return self.__logradouro
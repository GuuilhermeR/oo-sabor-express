from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
        
    @abstractmethod #todas classes derivadas precisam ter essa função, para essa classe, não importa como ela seja, só diz que todos tem que ter.
    def aplicar_desconto(self):
        pass
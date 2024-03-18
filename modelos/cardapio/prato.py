from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio): #Isso diz que o Prato é filho do ItemCardapio e que ele irá herdar classe, atributos do ItemCardapio.
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco) #O super ele permite que acessamos as informações de outras classes (métodos e atributos).
        self._descricacao=descricao
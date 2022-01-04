""""
Exemplo de uso do enum
    para escolher coisas sem sair do conjunto de coisas
    exemplo dum controle:
"""
from enum import Enum, auto


class Directions(Enum):
    right = auto()  # eu posso usar auto() para colocar um valor automaticamente
    left = auto()
    up = auto()
    down = auto()


def move(direction):
    if direction != 'right' and direction != 'left':
        """ 
        PB: se eu colocar novas direções tenho q modificar o if cada vez
        eu vou criar então um conjunto de coisas 
        """
        raise ValueError('Cannot move in this direction')

    return f'Moving {direction}'


def move_enum(direction):
    if not isinstance(direction, Directions):
        """ 
        Agora to vendo se a direção ta na class
        """
        raise ValueError('Cannot move in this direction')

    return f'Moving {direction.name} (name in Directions)', f'Valor do auto(): {direction.value}'


if __name__ == "__main__":
    print(move_enum(Directions.right))
    print(move_enum(Directions.left))
    print(move_enum(Directions.up))
    print(move_enum(Directions.down))

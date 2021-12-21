""""
Documentação em Python
É a primeira coisa do módulo
3 aspas duplas para inicializar (padrao pep8)
existem padrões de documentação
"""
import heranca_simples
import polimorfismo
import metodos_magicos


def funcao_documenta(x, y, z=0):
    """
    Geometria no espaço

    :param x: coordenada X
    :param y: coordenada Y
    :param z: Coordena Z (0 si 2D)
    :type: all floats or int

    :return: coordenadas do objeto
    :rtype: dict
    """
    return {'Abcisse': x, 'Ordonnée': y, 'Azimut': z}


# possso falar na assinatura da funcao o que eu quero tb:

def varios_tipos(a: int, b: float, c: str):
    return f'{c} é mais legal que {b} ou {a} '


def definir_return(a: int, b: float, c: str) -> str:  # posso dizer os tipos esperados e o tipo do retorno
    return 10  # PyCharm mostra q nao retorna o esperado

help(heranca_simples)
help(polimorfismo)
help(metodos_magicos)
help(funcao_documenta)

varios_tipos('pas int',4,8.5) # PyCharm mostra q tipo ta errado
""""
Documentação em Python
É a primeira coisa do módulo
3 aspas duplas para inicializar (padrao pep8)
existem padrões de documentação
"""
import heranca_simples
import polimorfismo
import metodos_magicos


def funcao_documenta(x, y, z = 0):
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


help(heranca_simples)
help(polimorfismo)
help(metodos_magicos)
help(funcao_documenta)

""" initialiser la commande dans le fichier, et écrire: python nom_du_fichier.py"""

import os
import sys

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('faltando argumentos')
    print('-a', 'Para listar todos os arquivos nessa pasta', sep='\t')
    print('-d', 'Para listar todos os diretorios nessa pasta', sep='\t')
    sys.exit()

so_arquivos = False
if '-a' in argumentos:
    so_arquivos = True

so_diretorios = False
if '-d' in argumentos:
    so_diretorios = True

for arquivo in os.listdir('.'):
    if so_arquivos:
        if os.path.isfile(arquivo):
            print(arquivo)

    if so_diretorios:
        if os.path.isdir(arquivo):
            print(arquivo)


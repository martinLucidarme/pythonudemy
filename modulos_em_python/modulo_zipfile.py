from zipfile import ZipFile
import os

caminho = r'C:\Users\Martin Lucidarme\Documents\moto'
with ZipFile('arquivo.zip', 'w') as zip1:  # a gente está escrevendo 'w'// criando o arquivo
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        zip1.write(caminho_completo, arquivo)
        # se eu colocar apenas o caminho, ele vai recriar o caminho inteiro no zip

with ZipFile('arquivo.zip', 'r') as zip2:  # a gente está lendo 'r' // lendo o arquivo
    for arquivo in zip2.namelist():
        print(arquivo)

with ZipFile('arquivo.zip', 'r') as zip3:
    zip3.extractall(f'{caminho}\descompactado')
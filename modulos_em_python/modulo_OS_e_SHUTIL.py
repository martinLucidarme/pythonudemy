import os
import shutil

caminho_original = r'C:\Users\Martin Lucidarme\Pictures\video OBS'
caminho_novo = r'C:\Users\Martin Lucidarme\Pictures\videoPython'

try:
    os.mkdir(caminho_novo)  # cria uma pasta
except FileExistsError as e:
    print(f'Pasta {caminho_novo} ja existe')

for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        # AGORA CUIDADO PARA NAO SOBRESCREVER O DELETAR ARQUIVOS SEM QUERER
        if 'ME' in file:
            shutil.copy(old_file_path, new_file_path)  # copiar arquiv
            print(f'Arquivo {file} copiado com sucesso')
            os.remove(new_file_path)  # apagar arquiv
            print(f'Arquivo {file} apagado com sucesso')

        shutil.move(old_file_path, new_file_path)  # desloca arquivos (ctrlXctrlV)
        print(f'Arquivo {file} movido com sucesso')

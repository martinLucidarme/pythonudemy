import os
from formata_tamanho_bytes import formata_tamanho

caminho_procura = input('Digite um Caminho: ')
termo_procura = input('Digite o termo que está procurando: ')

conta = 0
for raiz, diretorios, arquivos in os.walk(caminho_procura):  # walk: caminha no endereço
    for arquivo in arquivos:  # arquivos é uma lista de todos os 'arquivo'
        if termo_procura in arquivo:
            try:
                conta += 1
                caminho_completo = os.path.join(raiz, arquivo)  # o join junta nomes da pasta e arquivo
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)  # separa o arquivo e sua extensão
                tamanho = os.path.getsize(caminho_completo)  # tamanho em bytes
                print()
                print('Encontrei o arquivo:,', arquivo)
                print('No caminho: ', caminho_completo)
                print('Nome: ', nome_arquivo)
                print('Extensão: ', ext_arquivo)
                print('É de tamanho: ', tamanho)
                print(f'Ou seja: {formata_tamanho(tamanho)}')
            except PermissionError as e:
                print('Acesso restrito')
            except FileNotFoundError as e:
                print('Arquivo não encontrado')
            except Exception as e:
                print('Erro desconhecido', e)

print(f'\nForam encontrados {conta} arquivos')

# https://ffmpeg.zeranoe.com/builds/

"""
ffmpeg -i "ENTRADA" -i "LEGENDA" -c:v libx264 -crf23 -preset ultrafast -c:a aac -b:a 320k
-c:s srt -map v:0 -map a -map 1:0 -ss 00:00:00 -to 00:00:10 "SAIDA"

comandos do ffmpeg: entrada/legenda aac: encoder, -ss -to: momento do video a converter
"""

import os
import fnmatch
import sys

if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'
else:  # windows precisa baixart ffmpeg
    comando_ffmpeg = r'C:\ffmpeg\bin\ffmpeg.exe'

codec_video = '-c:v libx264'
codec_audio = '-c:a aac'
crf = '-crf 23'  # 18 melhor qld, 28 pior qld
preset = '-preset ultrafast'  # ultrafast: arquivos maiores
bitrate_audio = '-b:a 320k'
debug = ''  # para converter o video inteiro: debug = ''

caminho_origem = r'D:\video'
caminho_destino = r'C:\videoconvertido'
extensao_desejada = '.mkb'

for raiz, deps, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:
        if not fnmatch.fnmatch(arquivo, '*.mkv'):
            continue
        caminho_completo = os.path.join(raiz, arquivo)
        nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)
        print(nome_arquivo)
        caminho_legenda = nome_arquivo + '.srt'  # (para adicionar a legenda)
        print(caminho_completo)

        if os.path.isfile(caminho_legenda):  # ´para verificar existencia do arquivo
            input_legenda = f'-i "{caminho_legenda}"'
            map_legenda = '-c:s srt -map v:0 -map a - map1:0'  # mapeando video audio e legenda
        else:
            input_legenda = ''
            map_legenda = ''

        nom_arquivo, ext_arquivo = os.path.splitext(arquivo)
        arquivo_saida = rf'{caminho_destino}\{nom_arquivo}_NOVO{extensao_desejada}'

        comando = f'{comando_ffmpeg} -i "{caminho_completo}" {input_legenda} ' \
                  f'{codec_video} {crf} {preset} {codec_audio} {bitrate_audio} ' \
                  f'{debug} {map_legenda} "{arquivo_saida}"'

        os.system(comando)

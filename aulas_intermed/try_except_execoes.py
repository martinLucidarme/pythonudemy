'''
exeções
'''

try:
    a = 0
    try:
        a = 1/0
    except:
        print('Erro')

except NameError as erro:
    print('Erro do desenvolvedor:', erro)
except (IndexError, KeyError) as erro:
    print('Erro de indice')
except Exception as erro:
    print('Ocorreu um erro inesperado')
else:  # executado se nao tiver exeção
    print('To no else: codigo executado')
    print(a)
finally:  # executada sempre
    a = None  # se a da problema, voce resolve ele
    print(f'Finalmente, o "a" vai ser {a}')
print('Bora Continuar...')

perguntas = {
    'Pergunta 1 ': {
        'pergunta': 'Quanto é 2+2',
        'respostas' : {
            'a': '1',
            'b': '4',
            'c': '6',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2 ': {
        'pergunta': 'Quanto é 3*2',
        'respostas' : {
            'a': '10',
            'b': '4',
            'c': '6',
        },
        'resposta_certa': 'c',
    },
    'Pergunta 3 ': {
        'pergunta': 'Quanto é 4*4',
        'respostas' : {
            'a': '16',
            'b': '8',
            'c': '6',
        },
        'resposta_certa': 'a',
    },
}
respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Escolha a opção certa')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')
    resposta_usuario = input('Sua resposta:')

    if resposta_usuario == pv['resposta_certa']:
        print('está certo')
        respostas_certas += 1
    else:
        print('errou')

    print()
qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100
print(f'você acertou {respostas_certas}')
print(f'Sua porcentagem de acerto foi {porcentagem_acerto}%')
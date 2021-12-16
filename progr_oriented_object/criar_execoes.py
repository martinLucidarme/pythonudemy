class TaErradoError(Exception):  # Error no nome + Exception na assinatura
    pass


def testar():
    raise TaErradoError('Errado !')


try:
    testar()
except TaErradoError as error:
    print(f'Erro: {error}')

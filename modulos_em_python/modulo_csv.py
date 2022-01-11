"""
Comma Separated value
"""
import csv

with open('clientes.csv', 'r') as file:
    """
    PARA VER DADOS DO CSV
    dados = csv.reader(file)
    for dado in dados:
        print(dado)
    """

    """"
    PARA VER CSV COMO DICO E VER DADOS POR CHAVE
    dados_dico = csv.DictReader(file)
    for dado in dados_dico:
        print(dado['Nome'], dado['Sobrenome'], dado['E-mail'], dado['Telefone'])
    """
    dados2 = [x for x in csv.DictReader(file)]

with open('clientes2.csv', 'w') as file2:
    escreve = csv.writer(
        file2,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )

    # dados2 é uma lista de dicionario, dados[0] é o primeiro dico, pegos as keys desse dico
    chaves = dados2[0].keys()
    chaves = list(chaves)  # conveter as keys do primeiro dico em list
    escreve.writerow(
        [
            chaves[0],  # agora pode usar os indices numéricos
            chaves[1],
            chaves[2],
            chaves[3],
        ]
    )

    for dado in dados2:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone'],
            ]
        )

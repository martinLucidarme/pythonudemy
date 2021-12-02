"""
Faça una lista de tarefas com as seguintes opções
    add task
    list tasks
    desfazer ultima ação
    refazer ultima ação

    ['t1','t2','t3'] -> desfazer: ['t1','t2']
    ['t1','t2'] -> refazer:  ['t1','t2','t3']
"""
lista_tarefa = ['tarefa1', 'tarefa2']

nova_tarefa = input('Tarefa para adicionar')


def add_task(task,lista):
    lista.append(task)
    return lista


def desfazer(lista):
    lista_cancel = [lista.pop()]
    return lista_cancel, lista


def refazer(lista_cancel, lista):
    lista.append(lista_cancel[-1])
    lista_cancel.pop()
    return lista, lista_cancel


tirados = []
new_list = add_task(nova_tarefa, lista_tarefa)
print(new_list)
desfeita = desfazer(new_list)
print(desfeita[1])
tirados = tirados + desfeita[0]
refeita = refazer(tirados, new_list)
print(refeita[0])



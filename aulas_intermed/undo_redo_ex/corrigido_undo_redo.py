"""
Faça una lista de tarefas com as seguintes opções
    add task
    list tasks
    desfazer ultima ação
    refazer ultima ação

    ['t1','t2','t3'] -> desfazer: ['t1','t2']
    ['t1','t2'] -> refazer:  ['t1','t2','t3']
"""

# VERSAO CORRIGIDA / MAIS COMPLETA


def show_op(todo_list):
    print()
    print('Tarefas: ')
    print(todo_list)
    print()


def do_add(todo, todo_list):
    todo_list.append(todo)


def undo(todo_list, redo_list):
    if not todo_list:
        print('nada a desfazaer')
        return
    last_todo = todo_list.pop()
    redo_list.append(last_todo)


def redo(todo_list, redo_list):
    if not redo_list:
        print('nada a refazer')
        return
    last_redo = redo_list.pop()
    todo_list.append(last_redo)


if __name__ == '__main__':
    todo_list = []
    redo_list = []

    while True:
        todo = input('digite uma tarefa ou undo, redo , ls, stop: ')
        if todo == 'ls':
            show_op(todo_list)
            continue
        elif todo == 'undo':
            undo(todo_list,redo_list)
            continue
        elif todo == 'redo':
            redo(todo_list, redo_list)
            continue
        elif todo == 'stop':
            break
        do_add(todo, todo_list)
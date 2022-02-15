"""
Threads é para gestão dos processos,
controle da execução do codigo

CUIDADO QDO MANIP DADOS:
precisa usar locks para trancar os metodos em algum lugar

from threading import Lock
def metodo(x,y)
    self.lock.acquire()  => só um thread tem acesso ao metodo ao msm tempo

    'corpo da class'

    self.lock.release()
"""

from time import sleep
from threading import Thread


class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):  # sobescrivendo do Thread
        sleep(self.tempo)
        print(self.texto)


def meu_alvo(tex, tempo):
    sleep(tempo)
    print(tex)


# o Threads vao acontecer em determinados momentos do for i in range, nao necess na ordem
t1 = MeuThread('Thread 1', 9)
t1.start()

t2 = MeuThread('Thread 2', 5)
t2.start()

t3 = MeuThread('Thread 3', 2)
t3.start()

t = Thread(target=meu_alvo, args=('Thread parasito', 8))  # pode chamar args (tupla) e função
t.start()

for i in range(15):
    print(i)
    sleep(1)

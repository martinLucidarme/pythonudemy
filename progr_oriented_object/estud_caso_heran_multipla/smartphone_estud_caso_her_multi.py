from progr_oriented_object.estud_caso_heran_multipla.eletronico_estud_caso_her_multi import Eletronico
from progr_oriented_object.estud_caso_heran_multipla.log_estud_caso_her_multi import LogMixin


class Smartphone(Eletronico, LogMixin):  # herando tb da class Mixin que NAO VAI SER INSTANCIADA
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            info = f'{self._nome} nao esta ligado'
            print(info)
            self.log_info(info)
            return
        if self._conectado:
            error = f'{self._nome} ja está conectado'
            print(error)
            self.log_erro(error)
            return
        info = f'{self._nome} agora está conectado'
        self._conectado = True
        print(info)
        self.log_info(info)

    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} já NAO está conectado'
            print(error)
            self.log_erro(error)
            return
        info = f'{self._nome} foi desligado com sucesso'
        print(info)
        self.log_info(info)
        self._conectado = False

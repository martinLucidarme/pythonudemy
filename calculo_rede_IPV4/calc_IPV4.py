from function_num import sep_numero, decimal_para_binario, binario_para_decimal


class CalcRedeIPV4:
    def __init__(self, id='1.1.1.1', mascara='255.255.255.192'):
        self.id = id
        self.mascara = mascara

    def rede(self):
        list_num = sep_numero(self.id)
        ip_de_rede = f'{list_num[0]}.{list_num[1]}.{list_num[2]}.0'
        return ip_de_rede

    def broadcast(self):
        list_num = sep_numero(self.id)
        ultimo_mascara = sep_numero(self.mascara)[3]
        ultimo_broadcast = 255 - ultimo_mascara
        ip_de_broadcast = f'{list_num[0]}.{list_num[1]}.{list_num[2]}.{ultimo_broadcast}'
        return ip_de_broadcast

    def numero_de_redes(self):
        ultimo_mascara = sep_numero(self.mascara)[3]
        binar_ult_masc = decimal_para_binario(ultimo_mascara)
        contador = 0
        for z in binar_ult_masc:
            if z == '0':
                contador += 1
        numero_redes = (2 ** contador) - 2

        return numero_redes

    def primeira_ip(self):
        list_num = sep_numero(self.id)
        ip_inicial = f'{list_num[0]}.{list_num[1]}.{list_num[2]}.1'

        return ip_inicial

    def ultima_ip(self):
        list_num = sep_numero(self.id)
        ult_num = self.numero_de_hosts()
        ip_final = f'{list_num[0]}.{list_num[1]}.{list_num[2]}.{ult_num}'


        return ip_final
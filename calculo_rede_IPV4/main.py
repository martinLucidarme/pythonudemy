from calc_IPV4 import CalcRedeIPV4

if __name__ == '__main__':
    calc_ipv4 = CalcRedeIPV4('10.20.12.45', '255.255.255.240')
    print(f'A IP que temos é : {calc_ipv4.id}')
    print(f'A IP de rede é: {calc_ipv4.rede()}')
    print(f'A IP de broadcast é: {calc_ipv4.broadcast()}')
    print(f'A IP de máscara é : {calc_ipv4.mascara}')
    print(f'Numero de redes : {calc_ipv4.numero_de_redes()}')
    print(f'A primeira IP é: {calc_ipv4.primeira_ip()}')
    print(f'A ultima IO é: {calc_ipv4.ultima_ip()}')



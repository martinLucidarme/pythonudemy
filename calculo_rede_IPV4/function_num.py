def sep_numero(id_rede):
    num1 = ''
    num2 = ''
    num3 = ''
    num4 = ''
    generic = ''
    point = 0
    for v in id_rede:
        generic += v
        if v == '.':
            point += 1
            if point == 1:
                num1 = generic[:-1]
                generic = ''
            if point == 2:
                num2 = generic[:-1]
                generic = ''
            if point == 3:
                num3 = generic[:-1]
                generic = ''
        num4 = generic
    return [int(num1), int(num2), int(num3), int(num4)]


def decimal_para_binario(num):
    num_bin = ''
    list_bit = [128, 64, 32, 16, 8, 4, 2, 1]
    for bit in list_bit:
        if num < bit:
            num_bin += '0'
        elif num == bit:
            num_bin += '1'
            num = 0
        else:
            num = num - bit
            num_bin += '1'

    return num_bin


def binario_para_decimal(str_bin):
    num_dec = 0
    if str_bin[0] == '1':
        num_dec += 128
    if str_bin[1] == '1':
        num_dec += 64
    if str_bin[2] == '1':
        num_dec += 32
    if str_bin[3] == '1':
        num_dec += 16
    if str_bin[4] == '1':
        num_dec += 8
    if str_bin[5] == '1':
        num_dec += 4
    if str_bin[6] == '1':
        num_dec += 2
    if str_bin[7] == '1':
        num_dec += 1

    return num_dec

print(decimal_para_binario(192))

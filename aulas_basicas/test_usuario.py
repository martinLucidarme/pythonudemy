usuario= input('Digite o seu nome de usuario :')
qtd_carateres = len(usuario)

if qtd_carateres <6:
    print('usuario tem que ter no minimo 6 caracteres')
else :
    print('vc foi cadastrado(a)')
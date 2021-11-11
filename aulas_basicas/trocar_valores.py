
#  trocar variaveis: metodo complicado, outros codigos
x = 10
y = 'Luiz'

z = x
x = y
y = z

print(f'x={x}, y={y}')

# trocar em Python
a = 'primeiro a'
b = 'primeiro b'
a, b = b, a

print(f'a={a}, b={b}')

#(não tem limites de valor)

a, b, z, x, = x, z, b, a
print(f'a={a}, b={b}, z={z},x={x}')
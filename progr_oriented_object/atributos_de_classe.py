class A:
    vc = 123


class B:
    vcb = 123  # a class vai ficar com esse vcb

    def __init__(self):
        self.vcb = 321  # as instãncias vao ficar com esse vcb


print('--- Class A ---')
a1 = A()
a2 = A()

print(a1.vc, a2.vc)
print(A.vc)

A.vc = 321  # uso a class para mudar a variavel de class

print(a1.vc, a2.vc)
print(A.vc)

a1.vc = 456
print(a1.vc, a2.vc)  # apenas o vc da instancia a1 foi mudada
print(A.vc)

print(a1.__dict__, a2.__dict__)  # a vc foi salva no dict de a1 apenas, Py busca primeiro o vc na instancia, dps na cls

print('--- Class B ---')
b1 = B()
b2 = B()
print(b1.vcb, b2.vcb)  # as instancias ficaram com vcb do init
print(B.vcb)

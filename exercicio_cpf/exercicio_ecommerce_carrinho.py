'''
Site de E commerce, adiciona produtos a um carrinho
produtos tem variações
somar preço com list comprehension
'''
carrinho = []

carrinho.append(('Produto 1', 30.50))  # (Produto , preço)
carrinho.append(('Produto 2', '20'))
carrinho.append(('Produto 3', 50))

print(carrinho)
total = sum([float(y) for x, y in carrinho])
print(total)
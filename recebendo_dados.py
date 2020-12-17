""" Recebendo dados do usuário 
"""

# Entrada de Dados
print("Qual o Seu nome? ")
nome = input()  # Input -> Entrada

# Exemplo de print 'antigo' '2.x'
#print('Seja bem-vindo(a) %s' %nome)

# Exemplo de print 'moderno' 3.x
# print('Seja bem-vindo(a) {0}'.format{nome})

# Exemplo de print 'mais atual' 3.7
print(f'Seja bem-vindo {nome}')

print('Qual a sua idade?')
idade = input()

# processamento
print(f'{nome} tem {idade} anos')

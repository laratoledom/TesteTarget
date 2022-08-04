# Sequência de Fibonacci

# Sendo a Sequência de Fibonacci um conjunto de números infinitos, seria inviável a criação de uma lista (ou similar) com todos os seus elementos. 
# Assim, o ideal então, é definir primeiramente o número desejado e verificar se ele pertence a esse conjunto. 
# O número desejado (ou número informado) ficará a escolha do usuário, para que qualquer número seja aplicável ao programa.
# Chamaremos esse número de "n". O intuito é que a contagem dos números do conjunto seja feita somente até chegar no número informado n.
# O n_3 representará sempre o terceiro número, ou seja, a soma dos dois anteriores.
# Ao final da leitura, se o terceiro número (n_3) for igual ao número informado, então ele faz parte da Sequência de Fibonacci. Caso contrário, ele não faz parte.

n = int(input())
n_1 = 0
n_2 = 1
n_3 = n_1 + n_2

while n_3 < n:
    n_1 = n_2
    n_2 = n_3
    n_3 = n_1 + n_2

if n_3 == n:
    print("O número informado pertence à sequência")
else:
    print("O número informado não pertence à sequência")

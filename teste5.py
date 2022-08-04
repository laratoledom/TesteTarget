# A entrada ficará a critério do usuário para que qualquer palavra possa ser submetida ao programa.
# A lista "palavra_elementos" foi criada para que cada letra da palavra escolhida possa ser acessada como um único elemento.
# Também foi criada uma string vazia, "palavra_invertida", que irá juntar letra por letra da palavra invertida.

palavra = input()
palavra_elementos = []
palavra_invertida = ""
num_letras = len(palavra)

#Adicionando cada letra da palavra escolhida à lista "palavra_elementos"
i = 0
while i < num_letras:
    palavra_elementos.append(palavra[i])
    i = i + 1

#Transformando cada elemento da lista em uma string para que ela possa ser adicionada à "palavra_invertida"
for j in palavra_elementos:
    j = str(j)

#Adiciona-se o último elemento da lista à "palavra_invertida" e depois o mesmo é excluido, para que o penúltimo elemento passe a ser o último, e assim por diante.
k = 0
while k < num_letras:
    palavra_invertida = palavra_invertida + palavra_elementos[-1]
    palavra_elementos.pop(-1)
    k = k + 1

print(palavra_invertida)

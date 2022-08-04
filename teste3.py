#Faturamento de uma distribuidora

# Para essa atividade, foram utilizados os dados do arquivo json.
# Dados os dias do mês e seus respectivos faturamentos, foi montado um dicionário cuja chave representa os dias do mês e os
# valores das chaves representam o faturamento naquele dia.

faturamento_diario = {
    "dia_1": 22174.1664,
    "dia_2": 24537.6698,
    "dia_3": 26139.6134,
    "dia_4": 0.0,
    "dia_5": 0.0,
    "dia_6": 26742.6612,
    "dia_7": 0.0,
    "dia_8": 42889.2258,
    "dia_9": 46251.174,
    "dia_10": 11191.4722,
    "dia_11": 0.0,
    "dia_12": 0.0,
    "dia_13": 3847.4823,
    "dia_14": 373.7838,
    "dia_15": 2659.7563,
    "dia_16": 48924.2448,
    "dia_17": 18419.2614,
    "dia_18": 0.0,
    "dia_19": 0.0,
    "dia_20": 35240.1826,
    "dia_21": 43829.1667,
    "dia_22": 18235.6852,
    "dia_23": 4355.0662,
    "dia_24": 13327.1025,
    "dia_25": 0.0,
    "dia_26": 0.0,
    "dia_27": 25681.8318,
    "dia_28": 1718.1221,
    "dia_29": 13220.495,
    "dia_30": 8414.61
}

# Foi criada uma lista apenas com os valores dos faturamento diários, onde a ordem dos valores é respectiva aos dias do mês.
lista_de_valores = list(faturamento_diario.values())

# Primeiro, irei calcular o maior valor de faturamento, para que depois o programa possa retornar e encontrar o menor valor.
maior_valor = 0
menor_valor = 0
for i in lista_de_valores:
    if i > maior_valor:
        maior_valor = i
        menor_valor = i

# Para o cálculo do menor faturamento, serão ignorados os dias em que o faturamento é igual a zero, como orienta o enunciado.
for j in lista_de_valores:
    if j != 0:
        if j < menor_valor:
            menor_valor = j

#Uma nova lista é criada excluindo os valores iguais a zero para que a média possa ser calculada.
calculo_da_media = []
for k in lista_de_valores:
    if k != 0:
        calculo_da_media.append(k)

#Somando todos os valores de faturamento e encontrando a média final
soma_da_media = 0
l = 0
while l < len(calculo_da_media):
    soma_da_media = soma_da_media + calculo_da_media[l]
    l = l + 1

media_final = soma_da_media/len(calculo_da_media)

#Calculando o número de dias no mês em que o valor de faturamento diário foi superior à média mensal
num_dias = 0
for m in calculo_da_media:
    if m > media_final:
        num_dias = num_dias + 1

print("O menor valor de faturamento diário ocorrido esse mês foi:", menor_valor)
print("O maior valor de faturamento diário ocorrido esse mês foi:", maior_valor)
print("Número de dias no mês em que o valor de faturamento diário foi superior à média mensal:", num_dias)


# Observação: Caso fossem considerados os dias cujo valor de faturamento são iguais a zero, o menor valor de faturamentodiário ocorrido no mês teria sido zero.

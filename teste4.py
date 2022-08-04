#Foi calculado o valor total do faturamento, que representa 100% do mesmo, e a partir disso, o percentual de contribuição de cada estado.
SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
Outros = 19849.53

faturamento_total = SP + RJ + MG + ES + Outros

print("Percentual de SP:", (SP/faturamento_total)*100, "%")
print("Percentual de RJ:", (RJ/faturamento_total)*100, "%")
print("Percentual de MG:", (MG/faturamento_total)*100, "%")
print("Percentual de ES:", (ES/faturamento_total)*100, "%")
print("Percentual de Outros:", (Outros/faturamento_total)*100, "%")

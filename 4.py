Faturamento = {
    'SP' : 67836.43,
    'RJ' : 36678.66,
    'MG' : 29229.88,
    'ES' : 27165.48,
    'Outros' : 19849.53

}

total =  180759.98

print("Percentual de representação de cada estado:")
for estado, valor in Faturamento.items():
    percentual = (valor / total) * 100
    print(f"{estado}: {percentual:.2f}%")


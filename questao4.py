faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total = sum(faturamento.values())

for estado, valor in faturamento.items():
    percentual = (valor / total) * 100
    print(f"{estado} teve participação de {percentual:.2f}% no faturamento total.")

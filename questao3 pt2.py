import json

def calcular_faturamento():
    with open('faturamento.json', 'r') as file:
        dados = json.load(file)
    
    faturamento = [x for x in dados["faturamento_diario"] if x > 0]  # Ignorar dias sem faturamento
    menor_faturamento = min(faturamento)
    maior_faturamento = max(faturamento)
    media_faturamento = sum(faturamento) / len(faturamento)
    
    dias_acima_da_media = sum(1 for x in faturamento if x > media_faturamento)
    
    return menor_faturamento, maior_faturamento, dias_acima_da_media

menor, maior, dias_acima_media = calcular_faturamento()
print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Dias acima da média: {dias_acima_media}")

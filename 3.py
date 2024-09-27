import json

def processa_faturamento(dados_faturamento):

    dias_com_faturamento = [dia['valor'] for dia in dados_faturamento if dia['valor'] > 0]


    if not dias_com_faturamento:
        print("Nenhum dia com faturamento registrado.")
        return

    menor_faturamento = min(dias_com_faturamento)
    maior_faturamento = max(dias_com_faturamento)

    media_faturamento = sum(dias_com_faturamento) / len(dias_com_faturamento)

    dias_acima_da_media = sum(1 for valor in dias_com_faturamento if valor > media_faturamento)


    print(f"Menor faturamento do mês: R$ {menor_faturamento:.2f}")
    print(f"Maior faturamento do mês: R$ {maior_faturamento:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")


with open('faturamento.json', 'r') as arquivo_json:
    dados = json.load(arquivo_json)

processa_faturamento(dados['faturamento'])

import json
import os

# 1. Função para pedir o mês e o ano
def pedir_mes_e_ano():
    mes = input("Digite o mês (número): ").zfill(2)
    ano = input("Digite o ano (ex: 2025): ")
    return mes, ano

# 2. Função para carregar os clientes do arquivo JSON
def carregar_clientes():
    # Garante o caminho correto mesmo ao rodar pelo VS Code
    base_dir = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(base_dir, "config", "clientes.json")

    print(f"Carregando clientes de: {caminho_arquivo}")  # Debug opcional

    with open(caminho_arquivo, "r", encoding="utf-8") as file:
        return json.load(file)

# 3. Função para montar e criar o caminho com "MM - Nome"
def construir_caminho(pasta_base, ano, mes):
    meses = {
        "01": "Janeiro", "02": "Fevereiro", "03": "Março", "04": "Abril",
        "05": "Maio", "06": "Junho", "07": "Julho", "08": "Agosto",
        "09": "Setembro", "10": "Outubro", "11": "Novembro", "12": "Dezembro"
    }

    nome_mes = meses.get(mes, "Mês Inválido")
    if nome_mes == "Mês Inválido":
        raise ValueError("Número de mês inválido")

    pasta_mes = f"{mes} - {nome_mes}"
    caminho_final = os.path.join(pasta_base, ano, pasta_mes)

    if not os.path.exists(caminho_final):
        os.makedirs(caminho_final)
        print(f"Pasta criada: {caminho_final}")
    else:
        print(f"Pasta já existe: {caminho_final}")

    return caminho_final

# 4. Função principal
def main():
    mes, ano = pedir_mes_e_ano()
    clientes = carregar_clientes()

    for cliente in clientes:
        print(f"Processando cliente: {cliente['nome']}")
        caminho_final = construir_caminho(cliente["pasta_destino"], ano, mes)
        print(f"Relatórios deste cliente serão salvos em: {caminho_final}\n")

if __name__ == "__main__":
    main()

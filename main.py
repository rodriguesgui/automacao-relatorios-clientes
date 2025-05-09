import json
import os
from src.vetsoft import processar_vetsoft
# from src.clinicmanager import processar_clinicmanager  # Exemplo de outro sistema

# 1. Função para pedir o mês e o ano
def pedir_mes_e_ano():
    mes = input("Digite o mês (número): ").zfill(2)
    ano = input("Digite o ano (ex: 2025): ")
    return mes, ano

# 2. Carrega os clientes do JSON
def carregar_clientes():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(base_dir, "config", "clientes.json")
    print(f"Carregando clientes de: {caminho_arquivo}")
    with open(caminho_arquivo, "r", encoding="utf-8") as file:
        return json.load(file)

# 3. Cria a pasta no formato "ano/MM - NomeDoMês"
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

    if os.path.exists(caminho_final):
        arquivos = os.listdir(caminho_final)
        if arquivos:
            print(f"⚠️ A pasta '{caminho_final}' já existe e contém arquivos:")
            for arquivo in arquivos:
                print(f" - {arquivo}")
            continuar = input("Deseja substituir os arquivos? (s/n): ").strip().lower()
            if continuar != "s":
                print("⏭️  Pulando esse cliente.\n")
                return None
        else:
            print(f"Pasta já existe mas está vazia: {caminho_final}")
    else:
        os.makedirs(caminho_final)
        print(f"Pasta criada: {caminho_final}")

    return caminho_final

# 4. Redireciona para a função do sistema certo
def executar_por_sistema(cliente, caminho_destino):
    sistema = cliente.get("sistema", "").lower()
    if sistema == "vetsoft":
        processar_vetsoft(cliente, caminho_destino)
    # elif sistema == "clinicmanager":
    #     processar_clinicmanager(cliente, caminho_destino)
    else:
        print(f"⚠️  Sistema '{sistema}' ainda não suportado para o cliente {cliente['nome']}.")

# 5. Função principal
def main():
    mes, ano = pedir_mes_e_ano()
    clientes = carregar_clientes()
    for cliente in clientes:
        print(f"\n📋 Cliente: {cliente['nome']}")
        resposta = input("Deseja processar este cliente? (s/n): ").strip().lower()
        if resposta != "s":
            print(f"⏭️  Pulando {cliente['nome']}")
            continue

        caminho_final = construir_caminho(cliente["pasta_destino"], ano, mes)
        if not caminho_final:
            continue

        executar_por_sistema(cliente, caminho_final)
        print(f"✅ Finalizado: {cliente['nome']}\n")

if __name__ == "__main__":
    main()

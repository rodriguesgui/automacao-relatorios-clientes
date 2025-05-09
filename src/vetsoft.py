from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def processar_vetsoft(cliente, caminho_destino):
    print(f"🔧 Iniciando login no sistema Vetsoft para: {cliente['nome']}")
    print(f"➡️ Login: {cliente['login_url']} | Usuário: {cliente['usuario']}")
    print(f"📂 Pasta de destino: {caminho_destino}")

    # 1. Configura o navegador
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    # 2. Abre o navegador
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # 3. Vai até a URL de login
        driver.get(cliente["login_url"])
        time.sleep(2)

        # 4. Preenche os campos de login
        driver.find_element(By.ID, "usuario").send_keys(cliente["usuario"])
        driver.find_element(By.ID, "senha").send_keys(cliente["senha"])

        # 5. Clica no botão de login
        driver.find_element(By.ID, "btn-login").click()
        print("✅ Login enviado com sucesso")

        time.sleep(5)  # espera a próxima página carregar

        # Em breve: navegação até os relatórios e download
        print("📌 Aguardando próxima etapa (navegação até relatórios)")

    except Exception as e:
        print(f"❌ Erro durante o login: {e}")

    finally:
        pass  # ou comenta o driver.quit()



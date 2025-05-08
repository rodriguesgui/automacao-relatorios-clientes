# 📊 Automação de Relatórios para Clientes Veterinários

Este projeto tem como objetivo automatizar a rotina de extração, organização e armazenamento de relatórios mensais para clínicas veterinárias parceiras, utilizando Python.

---

## 🚧 Status: Em andamento

### ✅ Etapas já concluídas:
- [x] Estrutura modular inicial do projeto
- [x] Leitura dinâmica de dados dos clientes via arquivo `JSON`
- [x] Criação automática de pastas por ano e mês (`MM - Nome`) no Drive
- [x] Separação de dados sensíveis com uso de `.gitignore`

---

## 🛠️ Próximos passos:
- [ ] Automatizar login com Selenium para múltiplos sistemas
- [ ] Navegação até relatórios de vendas, clientes e origem
- [ ] Download automático dos arquivos
- [ ] Renomear arquivos por cliente, tipo e data
- [ ] Envio dos arquivos para pastas organizadas no Google Drive

---

## 🧱 Estrutura do projeto

```bash
automacao-relatorios/
├── main.py                     # Execução principal
├── config/
│   ├── clientes.json           # Dados reais (ignorado no Git)
│   └── clientes_exemplo.json   # Exemplo público
├── src/
│   ├── downloader.py           # (em breve) lógica de download
│   └── organizador.py          # movimentação de arquivos
├── relatorios/
├── temp_download/
└── .gitignore


💬 Sobre o autor
Desenvolvido por Guilherme Rodrigues, Analista de Dados/BI.
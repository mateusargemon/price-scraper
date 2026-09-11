| Arquivo / Pasta          | Função                                                                   |
| ------------------------ | ------------------------------------------------------------------------ |
| `main.py`                | Menu principal e centralização do sistema                                |
| `scraper.py`             | Coleta os dados da API e extrai/formata os preços                        |
| `storage.py`             | Registra os preços e a data em logs                                      |
| `analytics.py`           | Analisa os logs, calcula médias, identifica altas/baixas e emite alertas |
| `visualization.py`       | Gera o gráfico de linha com o histórico dos preços                       |
| `analysis/`              | Armazena as análises gerais geradas pelo `analytics.py`                  |
| `log/`                   | Armazena os registros individuais gerados pelo `storage.py`              |
| `scripts/`               | Armazena os scripts do projeto                                           |
| `resultado_scraper.json` | Arquivo intermediário entre `scraper.py` e `storage.py`                  |
| `README.md`              | Documentação e instruções básicas do projeto                             |
|

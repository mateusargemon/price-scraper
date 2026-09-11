import subprocess, sys, json, os, time
from datetime import datetime 

pasta_scripts = os.path.dirname(__file__) #define pasta pai dos .py

caminhoSC = os.path.join(pasta_scripts, "scraper.py")
caminhoST = os.path.join(pasta_scripts, "storage.py")
caminhoAN = os.path.join(pasta_scripts, "analytics.py")
caminhoVI = os.path.join(pasta_scripts, "visualization.py") #nao usado no def exec...() por ser opcional

def qtd_analises_realizadas(): #contabiliza quantidade de analises feitas

    try:
        with open("qty_analysis.txt","r") as qtyArchive:
            contador=int(qtyArchive.read())
    except FileNotFoundError:
        contador=0
    contador+=1
    with open("qty_analysis.txt","w") as qtyArchive1:
        qtyArchive1.write(str(contador))

def qtd_arquivos_gerados(): #conta quantidade de arquivos log e analysis gerado

    pasta_log = "log"
    qtd_log=len(os.listdir(pasta_log))
    
    pasta_ana = "analysis"
    qtd_ana=len(os.listdir(pasta_ana))

    print("\n" + "=" * 45)
    print(" " * 10 + "QUANTIDADE DE ARQUIVOS")
    print("=" * 45 + "\n")

    print(f"Pasta: {pasta_log} | Qtd: {qtd_log}")
    print(f"Pasta: {pasta_ana} | Qtd: {qtd_ana}")
    
    print("-" * 45 + "\n")
  
def limpar_tela(): #limpa tela 
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

def executar(): #executa analise (scraper->log->analysis)
    with open("qty_analysis.txt","r") as qtyArchive2:
        qtd_analises=int(qtyArchive2.read())
    print("\n" + "=" * 45)
    print(" " * 14 + "EXECUTANDO ANÁLISE Nº",qtd_analises)
    print("=" * 45 + "\n")

    subprocess.run([sys.executable, caminhoSC])
    subprocess.run([sys.executable, caminhoST])
    subprocess.run([sys.executable, caminhoAN])

    print("\n" + "=" * 45)
    print(" " * 14 + "ANÁLISE CONCLUÍDA")
    print("=" * 45 + "\n")

def gerar_grafico(): #gera grafico com visualization.py
    print("\n" + "=" * 45)
    print(" " * 16 + "GRÁFICO")
    print("=" * 45 + "\n")

    subprocess.run([sys.executable, caminhoVI])

def auto_exec(): #autoexecucao de analises
    while True:
        executar()
        time.sleep(600)

def relatorio_especifico(): #seleciona um log para visualizar
    print("\n" + "=" * 45)
    print(" " * 10 + "RELATÓRIO ESPECÍFICO")
    print("=" * 45 + "\n")

    pasta_log = "log"
    logs = sorted(
    os.listdir(pasta_log),
    key=lambda arquivo: datetime.strptime(
        arquivo.replace(".json", ""),
        "log_%d-%m-%Y_%Hh%M"
    ),
)
    for i, log in enumerate((logs)):
        print(f"  [{i}]  {log}")
    print()

    while True:
        try:
            escolha = int(input(">>> Sua escolha: "))
            arquivo_escolhido = logs[escolha]
            caminho = os.path.join(pasta_log, arquivo_escolhido)

            with open(caminho, "r") as arquivo:
                resultado = json.load(arquivo)
                break

        except (ValueError, IndexError):
            print("\n[!] Valor inválido.\n")

    print("\n" + "-" * 45)
    print(f"  ARQUIVO: {arquivo_escolhido}")
    print("-" * 45)

    print(f"| Produto          : {resultado['produto']}")
    print(f"| Data             : {resultado['data']}")
    print(f"| Parcelado (12x)  : R$ {resultado['parcelado']}")
    print(f"| Total parcelado  : R$ {resultado['total_parcelado']}")
    print(f"| À vista          : R$ {resultado['avista']}")

    print("-" * 45 + "\n")

def apagar_relatorios(): #apaga todos logs e analysis
    pasta_log = "log"
    pasta_ana = "analysis"
    caminhoL = pasta_log
    caminhoA = pasta_ana
    logs = sorted(
    os.listdir(pasta_log),
    key=lambda arquivo: datetime.strptime(
        arquivo.replace(".json", ""),
        "log_%d-%m-%Y_%Hh%M"
    ),
)
    anas = sorted(
    os.listdir(pasta_ana),
    key=lambda arquivo: datetime.strptime(
        arquivo.replace(".json", ""),
        "analysis_%d-%m-%Y_%Hh%M"
    ),
)
    for i in logs:
        os.remove(os.path.join("log", i))
    for j in anas:
        os.remove(os.path.join("analysis", j))

    print("\n[!] Registros apagados com sucesso.")

def relatorio_geral(): #seleciona uma analysis (resumo de varios logs) para visualizar
    print("\n" + "=" * 45)
    print(" " * 11 + "RELATÓRIO GERAL")
    print("=" * 45 + "\n")

    pasta_ana = "analysis"
    anas = sorted(
    os.listdir(pasta_ana),
    key=lambda arquivo: datetime.strptime(
        arquivo.replace(".json", ""),
        "analysis_%d-%m-%Y_%Hh%M"
    ),
)
    for i, ana in enumerate((anas)):
        print(f"  [{i}]  {ana}")

    print()

    while True:
        try:
            escolha = int(input(">>> Sua escolha: "))
            arquivo_escolhido = anas[(escolha)]
            caminho = os.path.join(pasta_ana, arquivo_escolhido)

            with open(caminho, "r") as arquivo:
                resultado = json.load(arquivo)
                break

        except (ValueError, IndexError):
            print("\n[!] Valor inválido.\n")

    print("\n" + "-" * 45)
    print(f"  ARQUIVO: {arquivo_escolhido}")
    print("-" * 45)

    print(f"| Data da Alta          : {resultado['maior'][0]}")
    print(f"| Alta à vista          : R$ {resultado['maior'][1][2]}")
    print()
    print(f"| Data da Baixa         : {resultado['menor'][0]}")
    print(f"| Alta à vista          : R$ {resultado['menor'][1][2]}")
    print()
    print(f"| Média à vista         : R$ {resultado['media_avista']:.2f}")
    print(f"| Média parcelado (12x) : R$ {resultado['media_total_parcelado']:.2f}")

    print("-" * 45 + "\n")

def menu(): #menu/inicio
    enter=False
    while True:
        while not enter:
            print()
            x=input("Pressione ENTER para continuar")
            print()
            limpar_tela()
            break

        print("\n" + "=" * 45)
        print(" " * 16 + "MENU PRINCIPAL")
        print("=" * 45)

        print("""
    [1] Executar análise
    [2] Autoanálise
    [3] Gerar gráfico 

    [4] Relatório específico 
    [5] Relatório geral 
    [6] Quantidade de arquivos gerados

    [7] Apagar registros
    
    [0] Sair
    """)

        print("-" * 45)

        escolha = input(">>> Sua escolha: ")

        if escolha == "1":
            limpar_tela()
            qtd_analises_realizadas() #nao chamar fora daqui para nao incrementar contador falsamente
            executar()

        elif escolha == "2":
            limpar_tela()
            auto_exec()

        elif escolha == "3":
            limpar_tela()
            gerar_grafico()

        elif escolha == "4":
            limpar_tela()
            relatorio_especifico()

        elif escolha == "5":
            limpar_tela()
            relatorio_geral()

        elif escolha == "6":
            limpar_tela()
            qtd_arquivos_gerados()

        elif escolha == "7":
            limpar_tela()
            apagar_relatorios()

        elif escolha == "0":
            limpar_tela()
            print("\nEncerrando...\n")
            break

        else:
            print("\n[!] Opção inválida.\n")
            time.sleep(2)
            enter=True

menu()

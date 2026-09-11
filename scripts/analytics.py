import json
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
import os

pasta_log = "log"
historico = {}

for logs in os.listdir(pasta_log):
    caminho = os.path.join(pasta_log, logs)

    with open(caminho, "r") as arquivo:
        historico[logs] = json.load(arquivo)

#print(json.dumps(historico, indent=4, ensure_ascii=False))

resultado = {}

cont = 0
soma_parcelado = 0
soma_total_parcelado = 0
soma_avista = 0

for registro in historico.values():
    data = registro["data"]
    parcelado = registro["parcelado"]
    total_parcelado = registro["total_parcelado"]
    avista = registro["avista"]

    resultado[data] = [float(parcelado), float(total_parcelado), float(avista)]

for data, precos1 in resultado.items():
    cont += 1
    soma_parcelado += (precos1[0])
    soma_total_parcelado += (precos1[1])
    soma_avista += (precos1[2])

maior = max(resultado.items(), key=lambda item: float(item[1][2]))
menor = min(resultado.items(), key=lambda item: float(item[1][2]))
maior_avista = maior[1][2]
menor_avista = menor[1][2]
nome_registro_maior = maior[0]
nome_registro_menor = menor[0]
valor_maior = float(maior[1][2])
valor_menor = float(menor[1][2])
valor_nominal=valor_maior-valor_menor
taxa_variacao=((valor_maior-valor_menor)/valor_menor)*100 # percentual

#print(f"X: maior {maior}")
#print(f"Y: menor {menor}")

media_avista = soma_avista / cont
media_parcelado = soma_parcelado / cont
media_total_parcelado = soma_total_parcelado / cont

resumo = {
    "maior": maior,
    "menor": menor,
    "media_avista": media_avista,
    "media_total_parcelado": media_total_parcelado
}

gmt_m3 = timezone(timedelta(hours=-3))
data_atual = datetime.now(gmt_m3)
data_atual = data_atual.strftime("%d-%m-%Y_%Hh%M")

nome_ana = ("analysis_" + data_atual + ".json").strip()
arquivo_ana = os.path.join("analysis", nome_ana)

with open(arquivo_ana, "w+") as archive:
    json.dump(resumo, archive, indent=4)


print("\n")
print("=" * 45)
print(">>> ANALYSIS")
print("=" * 45)
print()
print(f"| Data da Alta         : {nome_registro_maior}")
print(f"| Alta à vista         : R$ {maior_avista}")
print()
print(f"| Data da Baixa        : {nome_registro_menor}")
print(f"| Baixa à vista        : R$ {menor_avista}")
print()
print(f"| Média de preço       : R$ {media_total_parcelado:.2f}")
#print(f"| Média parcelado      : R${media_parcelado:.2f}")
print(f"| Variação Nominal     : R$ {valor_nominal:.2f}")
print(f"| Taxa de Variação     : {taxa_variacao:.2f}%")
print()
print("=" * 45)
print("\n")


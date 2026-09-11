import json,os,matplotlib.pyplot as plt,matplotlib.dates as mdates
from datetime import datetime

pasta_log = "log"
dados = []

# puxar os logs
for nome_arquivo in os.listdir(pasta_log):
    caminho = os.path.join(pasta_log, nome_arquivo)
    with open(caminho, "r", encoding="utf-8") as arquivo:
        registro = json.load(arquivo)

    data = datetime.strptime(
        registro["data"],
        "%d-%m-%Y_%Hh%M"
    )

    parcelado = float(registro["parcelado"])
    total_parcelado = float(registro["total_parcelado"])
    avista = float(registro["avista"])
    dados.append(
        (data, parcelado, total_parcelado, avista)
    )

# ordenar
dados.sort(key=lambda x: x[0])

# separar
datas = [x[0] for x in dados]
parcelados = [x[1] for x in dados]
totais = [x[2] for x in dados]
avistas = [x[3] for x in dados]

# criar grafico
plt.figure(figsize=(max(12, len(datas) * 0.4), 6))

plt.plot(
    datas,
    parcelados,
    marker="o",
    label="Parcelado"
)

plt.plot(
    datas,
    totais,
    marker="o",
    label="Total parcelado"
)

plt.plot(
    datas,
    avistas,
    marker="o",
    label="À vista"
)

# configs
plt.xlabel("Data")
plt.ylabel("Preço (R$)")
plt.title("Histórico de preços")
plt.legend()
plt.grid(True)

# eixo x
ax = plt.gca()

def mostrar_info(x, y):
    if not datas:
        return f"x={x:.2f}, y={y:.2f}"
    data_mouse = mdates.num2date(x).replace(tzinfo=None)

    indice = min(
        range(len(datas)),
        key=lambda i: abs(datas[i] - data_mouse)
    )

    data = datas[indice]
    return (
        f"Data: {data.strftime('%d/%m/%Y %H:%M')} | "
        f"Parcelado: R$ {parcelados[indice]:.2f} | "
        f"Total parcelado: R$ {totais[indice]:.2f} | "
        f"À vista: R$ {avistas[indice]:.2f}"
    )

ax.format_coord = mostrar_info
ax.set_xticks(datas)
ax.xaxis.set_major_formatter(
    mdates.DateFormatter("%d/%m/%Y %H:%M")
)

plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# titulo janela
manager = plt.get_current_fig_manager()

try:
    manager.window.title("GRAFICO ANALITICO")
except AttributeError:
    pass
plt.show()

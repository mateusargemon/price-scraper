import json
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
import os

gmt_m3 = timezone(timedelta(hours=-3))
data_atual = datetime.now(gmt_m3)
data_atual = data_atual.strftime("%d-%m-%Y_%Hh%M")

nome_log=("log_"+data_atual+".json").strip()
arquivo_preco="resultado_scraper.json"
arquivo_log=os.path.join("log",nome_log)

with open(arquivo_preco, "r") as archive:
        precos=json.load(archive)

precos["data"]=data_atual

with open(arquivo_log, "w+") as archive:
        json.dump(precos,archive,indent=4)

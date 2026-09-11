import requests
from bs4 import BeautifulSoup
import re
import json

url = "https://br.store.asus.com/notebook-asus-tuf-gaming-f16-fx608jhr-rv124-jaeger-gray.html"

r = requests.get(url, headers={
    "User-Agent": "Mozilla/5.0"
})

soup = BeautifulSoup(r.text, "html.parser")

texto = f"""
{soup}
"""

padrao = r"R\$\s*[\d.]+,\d{2}.*?À vista"

resultado = re.search(padrao, texto)

if resultado:
    precos_nao_formatados=resultado.group()
else:
    print("| API: Preços não encontrado")

html_preco=list(precos_nao_formatados)
preco_semi_formatado=[]

numeros_simbolos=["1","2","3","4","5","6","7","8","9","0",".",",","$"]
for i,l in enumerate(html_preco):
    if l in numeros_simbolos:
        preco_semi_formatado.append(l)

preco_quase_formatado="".join(preco_semi_formatado)
preco_quase_formatado = preco_quase_formatado.replace("$", " ").strip()
preco_formatado=preco_quase_formatado.split()

parcelado=preco_formatado[0]
total_parcelado=preco_formatado[1]
avista=preco_formatado[2]

parcelado = parcelado.replace(".", "").replace(",", ".")
total_parcelado = total_parcelado.replace(".", "").replace(",", ".")
avista = avista.replace(".", "").replace(",", ".")

precos={
    "produto":"FX608JHR-RV124",
    "data":"",
    "parcelado":parcelado,
    "total_parcelado":total_parcelado,
    "avista":avista
}

with open("resultado_scraper.json", "w") as archive:
        json.dump(precos, archive, indent=4)

#print(precos)

print("\n")
print("=" * 45)
print(">>> SCRAPER")
print("=" * 45)
print()
print("| Produto          :",precos["produto"])
print("| Parcelado (12x)  : R$", precos["parcelado"])
print("| Total parcelado  : R$", precos["total_parcelado"])
print("| À vista          : R$", precos["avista"])
print()
print("=" * 45)
print("\n")

# output: 
# R$ 666,58</span> <span class="label-installment">| 
# Total de</span> <span class="total-installment"
# ><span class="price">R$ 7.999,00</span></span>
#  <div class="iva">Impostos incluídos</div></span><span
#  class="price-management price-management-onetime"><span class="price">R$ 7.199,10</span> À vista




# R$ 7.999,00 R$ 11.999,00 Economize R$ 4.000,00 Ou 12x de R$ 666,58 | Total de R$ 7.999,00 Impostos incluídos R$ 7.199,10 À vista
import requests
from bs4 import BeautifulSoup

TOKEN = "8651548701:AAGN5qmWUS3jB_oj0kZOzB2_Oa9txnkDVwc"

CHAT_ID = "8180803690"
def enviar_telegram(mensaje):
    url_telegram = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    dato = {
        "chat_id": CHAT_ID,
        "text" : mensaje,
    }
    requests.post(url_telegram, data=dato)

url = "https://es.novelcool.com/novel/Kanojo-Okarishimasu.html"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Pop!_OS; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

respuesta = requests.get(url, headers=headers)

sopa = BeautifulSoup(respuesta.text, "html.parser")
capitulo = sopa.find("span", class_="chapter-item-headtitle")
if capitulo:
    capitulo_actual = capitulo.text.strip()
    memoria = ""
    try:
        with open("ultimo.txt","r") as archivo:
                memoria= archivo.read()
    except FileNotFoundError:
        pass
    if capitulo_actual != memoria:
        print(f"Rent a Girlfriend: {capitulo_actual}")
        enviar_telegram(f"📢 ¡Despierta! Nuevo capítulo de Kanojo Okarishimasu: {capitulo_actual}")
        with open("ultimo.txt", "w") as archivo: archivo.write(capitulo_actual)
    else:
        print("Todo sigue igual, a seguir esperando...")
else:
    print("¡Maldición, cambiaron el diseño!")
    
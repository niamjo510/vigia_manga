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

manga= {
    "Rent a Girlfriend":"https://es.novelcool.com/novel/Kanojo-Okarishimasu.html",
    "El Atelier De Sombreros De Mago": "https://es.novelcool.com/novel/El-Atelier-De-Sombreros-De-Mago.html",
    "One Piece":"https://manhwaweb.com/manga/one-piece_1695365223767",
    "Haimiya-senpai wa Kowakute Kawaii":"https://manhwaweb.com/manga/haimiya-senpai-wa-kowakute-kawaii_1762432488491",
    "Class De 2 Banme Ni Kawaii Onna No Ko To Tomodachi Ni Natta":"https://es.novelcool.com/novel/Class-De-2-Banme-Ni-Kawaii-Onna-No-Ko-To-Tomodachi-Ni-Natta.html",
    "Historias Que Ocurren Al Fumar En La Parte Trasera Del Supermercado":"https://manhwaweb.com/manga/historias-que-ocurren-al-fumar-en-la-parte-trasera-del-supermercado_1720409426443",
    "Otaku ni Yasashii Gyaru wa Inai!?":"https://manhwaweb.com/manga/otaku_ni_yasashii_gyaru_wa_inai!__1704173877239",
    "Mayonaka Heart Tune":"https://manhwaweb.com/manga/mayonaka-heart-tune-_1733372142895",
    "Mikadono Sanshimai Wa Angai, Choroi":"https://es.novelcool.com/novel/Mikadono-Sanshimai-Wa-Angai-Choroi.html",
    "Tamon-kun Ima Docchi?!":"https://es.novelcool.com/novel/Tamon-kun-Ima-Docchi.html",
    "Shiunji-ke No Kodomotachi":"https://es.novelcool.com/novel/Shiunji-ke-No-Kodomotachi.html",
    "A Couple Of Cuckoos":"https://es.novelcool.com/novel/A-Couple-Of-Cuckoos.html",
    "MARRIAGETOXIN":"https://es.novelcool.com/novel/MARRIAGETOXIN.html",
    "La Historia De Cuando Fui A Una Salida Grupal Y No Había Chicas":"https://es.novelcool.com/novel/La-Historia-De-Cuando-Fui-A-Una-Salida-Grupal-Y-No-Hab-a-Chicas.html",
    "Kaoru Hana Wa Rin To Saku":"https://manhwaweb.com/manga/kaoru_hana_wa_rin_to_saku_1703742073447",
    "Gachiakuta":"https://es.novelcool.com/novel/Gachiakuta.html",
    "Dandadan":"https://es.novelcool.com/novel/Dandadan.html",
    "Un cambio en mi vida: Tras ser engañado y acusado falsamente de un delito, la chica mas hermosa de la escuela se vuelve cercana a mi":"https://manhwaweb.com/manga/un-cambio-en-mi-vida-tras-ser-engaado-y-acusado-falsamente-de-un-delito-la-chica-mas-hermosa-de-la-escuela-se-vuelve-cercana-a-mi_1749331802901",
}
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Pop!_OS; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
for nombre, url in manga.items():
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
            print(f"{nombre}: {capitulo_actual}")
            enviar_telegram(f"📢 ¡Despierta! Nuevo capítulo de {nombre}: {capitulo_actual}")
            with open("ultimo.txt", "w") as archivo: archivo.write(capitulo_actual)
        else:
            print("Todo sigue igual, a seguir esperando...")
    else:
        print("¡Maldición, cambiaron el diseño!")
        
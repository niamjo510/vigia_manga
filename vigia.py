import requests
from bs4 import BeautifulSoup
import json
import os

# === CONFIGURACIÓN Y CONSTANTES ===
# Nota: En GitHub, la gente verá esto vacío. 
# Tú tendrás que poner tu token real solo en tu computadora.
TOKEN = "TU_TOKEN_SECRETO_AQUI" 
CHAT_ID = "TU_CHAT_ID_AQUI"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Pop!_OS; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Aquí va tu diccionario completo (ponlo tú)
MANGAS = {
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

# === FUNCIONES ===
def enviar_telegram(mensaje):
    """Envía un mensaje usando el bot de Telegram."""
    url_telegram = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    dato = {"chat_id": CHAT_ID, "text": mensaje}
    requests.post(url_telegram, data=dato)

def obtener_capitulo(url):
    """Extrae el número del capítulo dependiendo de la página web."""
    # === FASE 1: EXTRACCIÓN ===
    if "novelcool.com" in url:
        respuesta = requests.get(url, headers=HEADERS)
        sopa = BeautifulSoup(respuesta.text, "html.parser")
        etiqueta = sopa.find("span", class_="chapter-item-headtitle")
        # Si encuentra la etiqueta, saca el texto. Si no, lo deja en Nada (None)
        capitulo_actual = etiqueta.text.strip() if etiqueta else None

    elif "manhwaweb.com" in url:
        manga_id = url.split("/")[-1]
        api_url = f"https://manhwawebbackend-production.up.railway.app/manhwa/see/{manga_id}"
        respuesta_api = requests.get(api_url, headers=HEADERS)
        datos = respuesta_api.json()
        num = datos.get("_numero_cap", "??")
        capitulo_actual = f"Capitulo {num}"
        
    else:
        capitulo_actual = None
    return capitulo_actual
def cargar_memoria():
    """Carga el archivo JSON si existe, o devuelve un diccionario vacío."""
    try:
        with open("memoria.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

# === NÚCLEO DEL PROGRAMA ===
def main():
    print("Iniciando Vigía Manga...")
    historial = cargar_memoria()

    for nombre, url in MANGAS.items():
        print(f"Revisando: {nombre}...")
        capitulo_actual = obtener_capitulo(url)

        # Tu lógica de comparación y guardado (Fase 2 del código anterior)
        if capitulo_actual:
            capitulo_guardado = historial.get(nombre, "")
            if capitulo_actual != capitulo_guardado:
                print(f"📢 ¡Nuevo! {nombre}: {capitulo_actual}")
                enviar_telegram(f"📢 Nuevo capítulo de {nombre}: {capitulo_actual}")
                historial[nombre] = capitulo_actual
                
                with open("memoria.json", "w") as archivo:
                    json.dump(historial, archivo, indent=4)
            else:
                print(f"[{nombre}] Todo sigue igual.")
        else:
            print(f"⚠️ Error leyendo: {nombre}")

# Esta línea es la firma de un programador profesional en Python
# Le dice a Python: "Si ejecutan este archivo directamente, arranca el main()"
if __name__ == "__main__":
    main()
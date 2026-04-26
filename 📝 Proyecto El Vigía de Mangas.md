## 🛠️ Arquitectura Técnica

- **Lenguaje:** Python 3.
    
- **Librerías Core:** `requests` (red), `beautifulsoup4` (extracción de datos).
    
- **Infraestructura:** Docker (aislamiento) y Cron (programación horaria).
    
- **Notificación:** Discord/Telegram Webhooks.
    

---

## 🚩 Fase 1: El Extractor (Scraper Determinista)

**Meta:** Convertir una página web compleja en un simple número de capítulo.

- **Entrada:** URL de Novelcool de _Kanojo, Okarishimasu_.
    
- **Proceso:**
    
    1. Simular un navegador real (Headers/User-Agent).
        
    2. Descargar el código HTML crudo.
        
    3. Identificar y "limpiar" la etiqueta del capítulo más reciente.
        
- **Salida:** Un mensaje en terminal que diga: "Último capítulo detectado: [Número]".
    

## 🚩 Fase 2: La Memoria y el Aviso

**Meta:** Que el bot sepa si el capítulo es "nuevo" o si ya lo vimos.

- **Proceso:**
    
    1. Crear un archivo local `ultimo.txt` para guardar el número del último capítulo visto.
        
    2. Comparar el hallazgo de la Fase 1 con el archivo.
        
    3. **Si es mayor:** Actualizar el archivo y disparar un Webhook hacia un canal de Discord/Telegram.
        
    4. **Si es igual:** No hacer nada (dormir).
        

## 🚩 Fase 3: La Cápsula (Dockerización)

**Meta:** Que el bot funcione en cualquier sitio sin instalar nada en el sistema base.

- **Proceso:**
    
    1. Crear un `Dockerfile`.
        
    2. Definir la imagen base (Python-Slim).
        
    3. Configurar la instalación de dependencias automáticamente.
        
    4. Crear un "Volumen" para que la "Memoria" (`ultimo.txt`) no se borre al apagar el contenedor.
        

## 🚩 Fase 4: El Autómata (Cron)

**Meta:** Que el sistema trabaje solo mientras duermes.

- **Proceso:** Configurar una tarea programada en Pop!_OS que encienda el contenedor cada 6 horas.
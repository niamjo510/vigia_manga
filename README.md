# 👁️ Vigía Manga

Un bot de automatización desarrollado en Python para el monitoreo de actualizaciones de capítulos de manga. El sistema utiliza técnicas de **Web Scraping** y **Consumo de APIs** para enviar notificaciones instantáneas a Telegram.

## 🚀 Características principales

- **Enrutamiento Inteligente (Routing):** El bot identifica automáticamente el origen de la URL (Novelcool o Manhwaweb) y aplica la lógica de extracción adecuada.
- **Intercepción de APIs:** En sitios con contenido dinámico, el bot realiza ingeniería inversa para obtener los datos directamente desde el backend del servidor, optimizando el rendimiento.
- **Persistencia de Datos:** Implementación de un sistema de memoria en formato JSON para evitar notificaciones duplicadas y mantener un historial de lectura.
- **Arquitectura Modular:** Código organizado en funciones especializadas para facilitar la escalabilidad y el mantenimiento.

## 🛠️ Tecnologías y Herramientas

- **Lenguaje:** Python 3.10+
- **Librerías:** `BeautifulSoup4`, `requests`, `json`
- **Integración:** Telegram Bot API
- **Entorno de Desarrollo:** Pop!_OS / Linux Terminal


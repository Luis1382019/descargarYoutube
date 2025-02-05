import os
from yt_dlp import YoutubeDL

def download_video():
    video_url = input("Ingresa el link del video: ")

    # Ruta a la carpeta "Descargas" dentro del mismo directorio del script
    download_folder = os.path.join(os.getcwd(), "Descargas")

    # Crear la carpeta si no existe
    os.makedirs(download_folder, exist_ok=True)

    # Configuración de opciones para la descarga
    ydl_opts = {
        'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',  # Mejor calidad hasta 1080p
        'merge_output_format': 'mp4',  # Formato de salida
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),  # Ruta de salida en "Descargas"
        'verbose': True  # Mostrar información detallada
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            print("Iniciando descarga...")
            ydl.download([video_url])
            print(f"Descarga completada exitosamente en {download_folder}!")
    except Exception as e:
        print(f"Error durante la descarga: {str(e)}")

if __name__ == "__main__":
    download_video()

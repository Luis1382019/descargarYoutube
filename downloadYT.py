# Instalar venv
# 	sudo apt install python3-venv
# Crear entorno virtual
# 	python3 -m venv myenv
# Activar
# 	source myenv/bin/activate
# Desactivar/salir
# 	deactivate
	
# Librerias necesarias
# pip install yt-dlp

from yt_dlp import YoutubeDL

def download_video():
    video_url = input("Ingresa el link del video: ")
    
    # Configuración de opciones para la descarga
    ydl_opts = {
        'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',  # Mejor calidad hasta 1080p
        'merge_output_format': 'mp4',  # Formato de salida
        'outtmpl': '%(title)s.%(ext)s',  # Plantilla para el nombre del archivo
        'verbose': True  # Mostrar información detallada
    }
    
    try:
        with YoutubeDL(ydl_opts) as ydl:
            print("Iniciando descarga...")
            ydl.download([video_url])
            print("Descarga completada exitosamente!")
            
    except Exception as e:
        print(f"Error durante la descarga: {str(e)}")

if __name__ == "__main__":
    download_video()
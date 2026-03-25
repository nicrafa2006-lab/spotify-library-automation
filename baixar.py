import yt_dlp
import os
import time

def baixar_organizado(arquivo_txt):
    base_folder = 'Minhas_Musicas_MP3'
    
    if not os.path.exists(arquivo_txt):
        print(f" Erro: O arquivo {arquivo_txt} não foi encontrado!")
        return

    with open(arquivo_txt, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    print(f" Iniciando download de {len(linhas)} músicas restantes...")

    for i, linha in enumerate(linhas):
        linha = linha.strip()
        if not linha:
            continue

        try:
            # Separa Artista e Música
            if ' - ' in linha:
                partes = linha.split(' - ', 1)
                artista = partes[0].strip()
                musica = partes[1].strip()
            else:
                artista = "Outros"
                musica = linha

            # Cria a pasta do artista
            pasta_artista = os.path.join(base_folder, artista)
            if not os.path.exists(pasta_artista):
                os.makedirs(pasta_artista)

            # CONFIGURAÇÕES ANTI-BLOQUEIO
            ydl_opts = {
                'format': 'bestaudio/best',
                'noplaylist': True,
                # DIGITE O CAMINHO DA SUA PASTA BIN ABAIXO
                'ffmpeg_location': r'C:\Users\subzin\AppData\Local\ffmpegio\ffmpeg-downloader\ffmpeg\bin',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': f'{pasta_artista}/%(title)s.%(ext)s',
                'quiet': False,
                'sleep_interval': 5,
                'max_sleep_interval': 10,
            }

            print(f"\n--- [{i+1}/{len(linhas)}] PROCESSANDO: {linha} ---")
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                # O comando 'ytsearch1:' pega apenas o primeiro resultado da busca
                ydl.download([f"ytsearch1:{linha}"])
                
        except Exception as e:
            print(f" Erro ao processar '{linha}': {e}")
            # Se der erro de "Too Many Requests", o script para por 1 minuto para "esfriar"
            if "429" in str(e):
                print(" BLOQUEIO DETECTADO (429). Esperando 60 segundos para continuar...")
                time.sleep(60)

# EXECUÇÃO (Certifique-se de que o nome do arquivo abaixo é o de faltantes)
if __name__ == "__main__":
    baixar_organizado('musicas_faltantes.txt')
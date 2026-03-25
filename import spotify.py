import spotipy
from spotipy.oauth2 import SpotifyOAuth

# --- SUAS CHAVES ---
CLIENT_ID = 'seu client id aqui'
CLIENT_SECRET = 'seu client secret aqui' 
REDIRECT_URI = 'sua redirect uri aqui'

# --- CONEXÃO ---
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="user-library-read"
))

#ultilizando a biblioteca spotipy para acessar as músicas curtidas
def pegar_curtidas():
    musicas = []
    offset = 0
    print("Conectado! Vasculhando suas Músicas Curtidas...")
    
    while True:
        results = sp.current_user_saved_tracks(limit=50, offset=offset)
        items = results['items']
        if not items:
            break
        for item in items:
            track = item['track']
            musicas.append(f"{track['artists'][0]['name']} - {track['name']}")
        offset += len(items)
        print(f"Encontradas: {len(musicas)}")
    return musicas

# --- EXECUÇÃO ---
try:
    lista_final = pegar_curtidas()
    with open("minhas_curtidas.txt", "w", encoding="utf-8") as f:
        for m in lista_final:
            f.write(m + "\n")
    print("Arquivo 'minhas_curtidas.txt' criado com sucesso!")
except Exception as e:
    print(f"Erro: {e}")
import os

def verificar_faltantes(arquivo_original, pasta_musicas, arquivo_saida):
    #  Mapeia tudo dentro de todas as subpastas
    arquivos_encontrados = []
    if os.path.exists(pasta_musicas):
        for root, dirs, files in os.walk(pasta_musicas):
            for file in files:
                # Remove a extensão e guarda o nome em minúsculo para comparar
                nome_limpo = os.path.splitext(file)[0].lower()
                arquivos_encontrados.append(nome_limpo)

    #  Lê sua lista original
    with open(arquivo_original, 'r', encoding='utf-8') as f:
        lista_completa = [linha.strip() for linha in f.readlines() if linha.strip()]

    #  Compara os nomes
    faltantes = []
    for item in lista_completa:
        item_lower = item.lower()
        achou = False
        
        for arq in arquivos_encontrados:
            # Se o nome da lista estiver no nome do arquivo ou vice-versa
            if item_lower in arq or arq in item_lower:
                achou = True
                break
        
        if not achou:
            faltantes.append(item)

    #  Salva a nova lista
    with open(arquivo_saida, 'w', encoding='utf-8') as f:
        for item in faltantes:
            f.write(item + '\n')

    print(f" Conferência finalizada!")
    print(f" Pasta analisada: {pasta_musicas}")
    print(f" Músicas na lista original: {len(lista_completa)}")
    print(f" Arquivos totais encontrados: {len(arquivos_encontrados)}")
    print(f" Músicas faltando: {len(faltantes)}")

# Caminho correto conforme seu explorador de arquivos
caminho_musicas = os.path.join(os.getcwd(), 'Minhas_Musicas_MP3')
verificar_faltantes('minhas_curtidas.txt', caminho_musicas, 'musicas_faltantes.txt')
import unidecode

def rota_download_arquivo_geral(nomearquivohash, tipoarquivo):
    arquivo_geral = "https://conteudoava.unicesumar.edu.br/download/arquivo-geral/{}.{}/eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJzdWIiOiJqYXZhX2FwaV9jb250ZXVkb19uZXN0IiwiaWF0IjoxNTAxMjY5NDc5LCJleHAiOjI0NDczNDk0Nzl9.pHS0ftTRrtEtB-iUKKMaIJX8-6DutLn5zpalZYipC_upQIoCgWF165JeTcC5q568vH86zcoqOcs2CI6mmpfnMQ".format(nomearquivohash, tipoarquivo)
    return arquivo_geral


def nome_arquivo_safe(arquivo):
    arquivo: str
    arquivo = arquivo.replace('\\', '_')
    arquivo = arquivo.replace('/', '_')
    arquivo = arquivo.replace('|', '_')
    arquivo = arquivo.replace('?', '_')
    arquivo = arquivo.replace('<', '_')
    arquivo = arquivo.replace('>', '_')
    arquivo = arquivo.replace('*', '_')
    arquivo = arquivo.replace(':', '_')
    arquivo = arquivo.replace('"', '_')
    arquivo = arquivo.replace(' ', '_')
    arquivo = arquivo.replace('-', '_')
    arquivo = arquivo.replace('–', '_')
    arquivo = arquivo.replace('__', '_')
    arquivo = arquivo.replace('__', '_')
    arquivo = arquivo.lower()
    arquivo = unidecode.unidecode(arquivo)
    return arquivo[:256]

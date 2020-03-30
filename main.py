import requests
from config import MATERIAS
from dotenv import load_dotenv
import os
load_dotenv()
print('Carregando Imports...')

directory_pwd = os.getenv('DIRECTORY_UNIVERSIDADE')
print('Você utilizou a configuração com senha, ou com IDs de transmissão?')
app_version = input('1 - SENHA | 2 - ARQUIVO IDs de Transmissão! -> ')

if int(app_version) == 2:
    for materia in MATERIAS:
        temp_dir_materia = directory_pwd + '/{}'.format(materia)
        temp_dir_materia_verify = os.path.isdir(temp_dir_materia)
        if not temp_dir_materia_verify:
            os.mkdir(temp_dir_materia)
        for aula in MATERIAS[materia]:
            temp_dir_aula = temp_dir_materia + '/{}'.format(aula)
            temp_dir_aula_verify = os.path.isdir(temp_dir_aula)
            if not temp_dir_aula_verify:
                os.mkdir(temp_dir_aula)
            transmission_id = MATERIAS[materia][aula]
            page_exist = True
            counter = 1
            while page_exist:
                temp_dir_slide = temp_dir_aula + '/Imagem{}.jpg'.format(counter)
                if os.path.isfile(temp_dir_slide):
                    continue
                URL = 'http://video.ead.cesumar.br/transmissoes/{}/slides/Imagem{}.jpg'.format(transmission_id, counter)
                get_page = requests.get(URL)
                if get_page.status_code == 200:
                    with open(temp_dir_slide, 'wb') as file:
                        for chunk in get_page.iter_content(1024):
                            file.write(chunk)
                    counter += 1
                elif get_page.status_code == 404:
                    page_exist = False

elif int(app_version) == 1:
    print('Versão não disponível!')

else:
    print('Versão não encontrada!')

print('Procedimento finalizado...')

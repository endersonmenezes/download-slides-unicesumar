import os
import time

import requests

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from auxiliar.funcoes import rota_download_arquivo_geral, nome_arquivo_safe

from selenium.common.exceptions import TimeoutException


def procedimento_baixar_arquivos(webdrive, wait, rota, directory_pwd, geral, nome_disciplina):
    # TODO Estamos utilizando GERAL(BOOL) para controlar, porém a rota é a mesma, parece que pegamos o XPATH incorreto. Realizar mais testes
    webdrive.get(rota)
    if geral:
        elemento_arquivos = '/html/body/div[2]/div/div[2]/div[1]/div/ui-view/ui-view/ui-view/div/div/div[2]/div/div[1]/div'
    else:
        elemento_arquivos = '/html/body/div[2]/div/div[2]/div[1]/div/ui-view/ui-view/ui-view/div/div/div/div[2]/div/div[1]/div'
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, elemento_arquivos)))
        time.sleep(2)
        # TODO Trocar o time.sleep() por uma função que corresponde melhor o tempo de carregamento das variaveis do Angular
        if geral:
            console_script = 'return angular.element(document.querySelector("#content > div > ui-view > ui-view > ui-view > div")).scope().vm.arquivos'
        else:
            console_script = 'return angular.element(document.querySelector("#content > div > ui-view > ui-view > ui-view > div > div > div")).scope().vm.arquivos'
        arquivos_gerais = webdrive.execute_script(console_script)
        if not os.path.isdir(directory_pwd):
            os.makedirs(directory_pwd)
        for arquivo in arquivos_gerais:
            link_download = rota_download_arquivo_geral(arquivo['nomeArquivoHash'], arquivo['tipo'])
            r_page = requests.get(link_download, stream=True)
            tmp_pwd = '{}/{}.{}'.format(directory_pwd, nome_arquivo_safe(arquivo['descricao']), arquivo['tipo'])
            with open(tmp_pwd, 'wb') as file:
                for chunk in r_page.iter_content(1000):
                    file.write(chunk)
            print(f'{nome_disciplina}: {arquivo["descricao"]} - Baixado!')
    except TimeoutException:
        pass

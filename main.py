import requests
from dotenv import load_dotenv
import os
import time
import json
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
print('Carregando Imports...')

load_dotenv()
directory_pwd = os.getenv('DIRECTORY_UNIVERSIDADE')
user_ra = os.getenv('USER_RA')
user_pass = os.getenv('USER_SENHA')
os_user = os.getenv('OS_USER')
print('Carregando váriaveis de ambiente...')

rota_login = "https://studeo.unicesumar.edu.br/"
rota_arquivos_gerais = "https://studeo.unicesumar.edu.br/#!/app/studeo/aluno/ambiente/arquivo-geral"


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
    return arquivo

print('Carregando rotas...')

webdrive_options = webdriver.FirefoxOptions()
webdrive_options.add_argument('-headless')
webdrive_options.add_argument('-no-sandbox')
webdrive_options.add_argument('-disable-dev-shm-usage')

if os_user == "W":
    webdrive = webdriver.Chrome('drivers/geckodriver.exe', options=webdrive_options)
else:
    webdrive = webdriver.Chrome('drivers/geckodriver', options=webdrive_options)

wait = WebDriverWait(webdrive, 10)
print('Webdrive configurado...')

webdrive.get(rota_login)
wait.until(EC.element_to_be_clickable((By.ID, 'username')))
wait.until(EC.element_to_be_clickable((By.ID, 'password')))
webdrive.find_element(By.ID, "username").send_keys(user_ra)
webdrive.find_element(By.ID, "password").send_keys(user_pass)
webdrive.find_element(By.CSS_SELECTOR, ".btn").click()
print('Login efetuado com sucesso...')

try:
    btn_avisos = 'Ignorar avisos'
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="{}"]'.format(btn_avisos)))).click()
except:
    pass
# TODO Configurar as exceções corretamentes, para não "vazar" um erro qualquer.
print('Pulando os avisos com sucesso...')

webdrive.get(rota_arquivos_gerais)

elemento_arquivos = '/html/body/div[2]/div/div[2]/div[1]/div/ui-view/ui-view/ui-view/div/div/div[2]/div/div[1]/div'
wait.until(EC.presence_of_element_located((By.XPATH, elemento_arquivos)))
time.sleep(2)
console_script = 'return angular.element(document.querySelector("#content > div > ui-view > ui-view > ui-view > div > div")).scope().vm.arquivos'
arquivos_gerais = webdrive.execute_script(console_script)
os.makedirs('{}/arquivos-gerais'.format(directory_pwd))
for arquivo in arquivos_gerais:
    link_download = rota_download_arquivo_geral(arquivo['nomeArquivoHash'], arquivo['tipo'])
    r_page = requests.get(link_download, stream=True)
    tmp_pwd = '{}/arquivos-gerais/{}.{}'.format(directory_pwd, nome_arquivo_safe(arquivo['descricao'])[0:256], arquivo['tipo'])
    with open(tmp_pwd, 'wb') as file:
        for chunk in r_page.iter_content(1000):
            file.write(chunk)
    print('Arquivo Geral: {} - Baixado!'.format(arquivo['descricao']))

# elemento_arquivos = webdrive.find_element_by_xpath(elemento_arquivos)

# for element in elemento_arquivos:
#     print(element.text)

# print(elemento_arquivos.get_attribute('innerHTML'))
# webdrive.quit()
print('Webdrive encerrado, fim de código.')

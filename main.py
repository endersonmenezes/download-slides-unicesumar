import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from auxiliar.funcoes import nome_arquivo_safe
from auxiliar.procedimentos import procedimento_baixar_arquivos

print('UniCesumar Download - Um facilitador para o uso do Studeo!')
print('Carregando imports...')

DOCKER_ON = os.getenv('DOCKER_ON', None)
if DOCKER_ON:
    display = Display(visible=0, size=(800, 600))
    display.start()
    print('Carregando display virtual...')

load_dotenv()
directory_pwd = os.getenv('DIRECTORY_FILES')
user_ra = os.getenv('STUDEO_USER')
user_pass = os.getenv('STUDEO_PASS')
os_user = os.getenv('OS_USER')
print('Carregando váriaveis de ambiente...')

rota_login = "https://studeo.unicesumar.edu.br/"
rota_arquivos_gerais = "https://studeo.unicesumar.edu.br/#!/app/studeo/aluno/ambiente/arquivo-geral"
rota_disciplinas = "https://studeo.unicesumar.edu.br/#!/app/studeo/aluno/ambiente/disciplina"
rota_interna_disciplinas = 'https://studeo.unicesumar.edu.br/#!/app/studeo/aluno/ambiente/disciplina/'
print('Carregando rotas...')

webdrive_options = webdriver.FirefoxOptions()
webdrive_options.add_argument('-headless')
webdrive_options.add_argument('-no-sandbox')
webdrive_options.add_argument('-disable-dev-shm-usage')

webdrive = webdriver.Firefox(options=webdrive_options)

wait = WebDriverWait(webdrive, 10)
print('Configurando webdriver...')

webdrive.get(rota_login)
wait.until(EC.element_to_be_clickable((By.ID, 'username')))
wait.until(EC.element_to_be_clickable((By.ID, 'password')))
webdrive.find_element(By.ID, "username").send_keys(user_ra)
webdrive.find_element(By.ID, "password").send_keys(user_pass)
webdrive.find_element(By.CSS_SELECTOR, ".btn").click()
print('Efetuando login...')

try:
    btn_avisos = 'Ignorar avisos'
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="{}"]'.format(btn_avisos)))).click()
    print('Fechando janela de avisos...')
except:
    pass
# TODO Configurar as exceções corretamentes, para não "vazar" um erro qualquer.

# BAIXANDO ARQUIVOS GERAIS - BEGIN
pwd_arquivos_gerais = '{}/arquivos_gerais'.format(directory_pwd)
procedimento_baixar_arquivos(webdrive, wait, rota_arquivos_gerais, pwd_arquivos_gerais, geral=True)
# BAIXANDO ARQUIVOS GERAIS - END

# BAIXANDO ARQUIVOS DAS DISCIPLINAS - BEGIN
webdrive.get(rota_disciplinas)
elemento_disciplinas = '/html/body/div[2]/div/div[2]/div[1]/div/ui-view/ui-view/ui-view/div/div/div[2]/div/div[1]/div'
wait.until(EC.presence_of_element_located((By.XPATH, elemento_disciplinas)))
time.sleep(10)
# TODO Trocar o time.sleep() por uma função que corresponde melhor o tempo de carregamento das variaveis do Angular
console_script = 'return angular.element(document.querySelector("#panel1")).scope().vm.disciplinas'
disciplinas = webdrive.execute_script(console_script)
pwd_disciplinas = '{}/disciplinas'.format(directory_pwd)
if not os.path.isdir(pwd_disciplinas):
    os.makedirs(pwd_disciplinas)
for disciplina in disciplinas:
    if disciplina['tpMatricula'] == 'matriculado':
        link_disciplina = '{}{}'.format(rota_interna_disciplinas, disciplina['cdShortname'])
        link_disciplina_arquivos = '{}{}/{}'.format(rota_interna_disciplinas, disciplina['cdShortname'], disciplina['cdShortname'])
        nome_pasta = nome_arquivo_safe(disciplina['nmDisciplina'])
        pwd_materia_tmp = '{}/{}'.format(pwd_disciplinas, nome_pasta)
        procedimento_baixar_arquivos(webdrive, wait, link_disciplina_arquivos, pwd_materia_tmp, geral=False)

# BAIXANDO ARQUIVOS DAS DISCIPLINAS - END


# elemento_arquivos = webdrive.find_element_by_xpath(elemento_arquivos)

# for element in elemento_arquivos:
#     print(element.text)

# print(elemento_arquivos.get_attribute('innerHTML'))
webdrive.quit()
if DOCKER_ON:
    display.stop()
print('Webdrive encerrado, fim de código.')

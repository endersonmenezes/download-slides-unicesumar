# Download UniCesumar (EaD)
Script para baixar todos os materiais e conteudos disponíveis para você, além de organizar isso em um diretório que você deseja.


**Esse script não visa quebrar nenhum direito, ou normas da Instituição.
Apenas automatizar o processo de Download dentro do Studeo.**

# Selenium

A pasta /drivers/ contém os drivers para Win64 e Linux64 utlizando Firefox. [Clique aqui](https://github.com/mozilla/geckodriver/releases) se você deseja consultar a fonte desses arquivos.

## Como configurar?

Crie um arquivo *.env* no mesmo diretório e utilize a configuração abaixo:

```.env
DIRECTORY_UNIVERSIDADE="C:/Users/ender/Desktop/Pasta_Universidade"
USER_RA="******"
USER_SENHA="*******"
OS_USER="W"
```
**Atenção nao termine com "/" e utilize as barras conforme exemplo**

O campo **OS_USER** deve ser preenchido com "W" para Windows e "L" para Linux.
## Como executar?
Desenvolvido e testado com **Python 3.8.5**, recomenda-se utilização de uma venv para execução.
 
Para criar uma venv

```.shell script
python3.8 -m venv venv
source venv/bin/activate
```

Digite para abrir o script:

```.shell script
python -m pip install -r requirements.txt
python main.py
```

## Executável no Windows


## Como colaborar?

Sinta-se livre para colaborar, estou ajeitando o código, crie uma **Issue** e conversamos :)

## TODO

- [X] Autenticação com Login e Senha;
- [X] Login via Selenium;
- [X] Função Download dos Materiais do curso;
- [X] Função Download dos Materiais de cada materia;
- [ ] Desenvolvimento EXE para Windows;
- [ ] Perceber quais materias são EAD e possuem video-aulas para baixar os slides;
- [ ] Customizar essa opções para usuário em um Menu.
- [ ] Remover código não comentado
- [ ] Preparar versão beta
- [ ] Criar manual para utilização do GoogleColab

# Download UniCesumar (EaD)
Script para baixar todos os materiais e conteudos disponíveis para você, além de organizar isso em um diretório que você deseja. Eu utilizo o PyCharm estão se você utilizar também recebera algumas configurações ao abrir o projeto.

**Esse script não visa quebrar nenhum direito, ou normas da Instituição.
Apenas automatizar o processo de Download dentro do Studeo.**

# Como utilizar?

## Como configurar?

Crie um arquivo *.env* no mesmo diretório e utilize a configuração abaixo:

```.env
STUDEO_USER=""
STUDEO_PASS=""
```

Preencha com seu usuário e sua senha do Studeo.

## Como executar?
Basta você ter o Docker instalado em seu computador. Se você utiliza Windows, [esse site](https://docs.docker.com/docker-for-windows/install/) pode te ajudar.

````bash
# Digite o comando abaixo para criar a máquina.
docker-compose build

# Digite o comando abaixo para rodar o script, lembre-se de configurar o .env
docker-compose up
````

## Como colaborar?

Sinta-se livre para colaborar, estou ajeitando o código, crie uma **Issue** e conversamos :)

## TODO

- [X] Autenticação com Login e Senha;
- [X] Login via Selenium;
- [X] Função Download dos Materiais do curso;
- [X] Função Download dos Materiais de cada matéria;
- [ ] Desenvolvimento EXE para Windows;
- [ ] Perceber quais materias são EAD e possuem video-aulas para baixar os slides;
- [ ] Customizar essa opções para usuário em um Menu;
- [ ] Remover código não comentado;
- [ ] Preparar versão beta;
- [ ] Criar manual para utilização do GoogleColab;
- [X] Criar versão utilizando o Docker;

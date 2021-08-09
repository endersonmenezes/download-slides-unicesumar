# Download UniCesumar (EaD)
Script para baixar todos os materiais e conteudos disponíveis para você, além de organizar isso em um diretório que você deseja. Eu utilizo o PyCharm estão se você utilizar também recebera algumas configurações ao abrir o projeto.

**Esse script não visa quebrar nenhum direito, ou normas da Instituição.
Apenas automatizar o processo de Download dentro do Studeo.**

# Como utilizar?

## Como configurar?
Instale git no seu computador, ou faça o download dos arquivos. [Clique aqui](https://git-scm.com/downloads) para baixar o Git.

````bash
git clone https://github.com/endersonmenezes/download-slides-unicesumar.git
````
Na pasta que o git criou, ou que você extrair os arquivos baixados, crie um arquivo com o nome **.env** e cole o texto abaixo:

```.env
STUDEO_USER=""
STUDEO_PASS=""
DIRECTORY_FILES=""
```

Preencha com seu usuário e sua senha do Studeo.
Para criar o arquivo, você pode utilizar o bloco de notas, lembre-se de alterar a extensão dele.
O campo `DIRECTORY_FILES` refere-se aonde você quer que o download de materiais seja realizado.

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

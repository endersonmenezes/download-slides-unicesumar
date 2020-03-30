# Slides UniCesumar (EaD)
Script para baixar os slides de uma aula EaD da UniCesumar.
Esse script não visa quebrar nenhum direito, ou normas da Instituição.
Apenas automatizar o processo de Download de Slides das Aulas EaD.


## Como configurar?

Crie um arquivo chamado **config.py** e siga o seguinte modelo:

```python
MATERIAS = {}

MATERIAS['nome_da_pasta_que_voce_deseja'] = {
    'aula01':'idTransmissao01',
    'aula02':'idTransmissao02',
}

MATERIAS['nome_da_pasta_que_voce_deseja_2'] = {
    'aula01':'idTransmissao01',
    'aula02':'idTransmissao02',
}
```

Crie um arquivo *.env* no mesmo diretório e utilize a configuração abaixo:

```.env
DIRECTORY_UNIVERSIDADE="C:\Users\ender\Google Drive\UniCesumar\Universidade\EAD Modulos"
STUDEO_USER="******"
STUDEO_PASS="*******"
```

Não se preocupe em preencher a sua senha e usuário, esse modulo ainda não funciona mesmo :)

## Como executar?

Digite para abrir o script:

```.shell script
python main.py
```

## Como colaborar?

Sinta-se livre para colaborar, estou ajeitando o código, crie uma **Issue** e conversamos :)


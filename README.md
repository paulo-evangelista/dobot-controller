[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/)



# dobot-controller
Plataforma que permite controlar o Dobot Magician Lite, com um modelo 3D em tempo real

## Para iniciar a api (em modo de desenvolvimento), execute os comandos abaixo, em ordem, no terminal dentro da pasta `dobot-controller`

`cd backend`

`python -m venv venv`

`cd venv\Scripts`

- Caso esteja utilizando o PowerShell, rode `.\Activate.ps1`
- Caso esteja utilizando o Command Prompt, rode `activate.bat`

`cd ..\..\api`

`pip install -r requirements.txt`

`cd ..`

`prisma generate`

`cd api`

- Agora, conecte o Dobot Magician e ligue-o

`python app.py`

### Pronto! agora é só acessar a pasta `executable` e executar a interface!

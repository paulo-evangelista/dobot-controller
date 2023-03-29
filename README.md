[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/)



# dobot-controller
Plataforma que permite controlar o Dobot Magician Lite, com um modelo 3D em tempo real

- **Vídeo demonstração:** https://photos.app.goo.gl/du6HN2J5HaDLSP2s7


## Para iniciar a api (em modo de desenvolvimento), execute os comandos abaixo, em ordem, no terminal dentro da pasta `dobot-controller`

1° - `cd backend`

2° - `python -m venv venv`

3° - `cd venv\Scripts`

4° -  Caso esteja utilizando o PowerShell, rode `.\Activate.ps1`
   -  Caso esteja utilizando o Command Prompt, rode `activate.bat`

5° - `cd ..\..\api`

6° - `pip install -r requirements.txt`

7° - `cd ..`

8° - `prisma generate`

9° - `cd api`

- Agora, conecte o Dobot Magician e ligue-o

10° - `python app.py`

### Pronto! agora é só acessar a pasta `executable` e executar a interface!

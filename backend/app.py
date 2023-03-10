from flask import Flask, request
from controller import Controller
from serial.tools import list_ports


# dobot = Controller()

app = Flask(__name__)
dobotPort = "COM7"

print("--------------------------------------------------")
print("Servidor iniciando...")
print("--------------------------------------------------")
available_ports = list_ports.comports()
print(f'Portas de comunicação disponíveis: {[x.device for x in available_ports]}')
print("--------------------------------------------------")
print(f"Conectando ao Dobot Magician Lite na porta {dobotPort}...")
print("--------------------------------------------------")

try:
    dobot = Controller(dobotPort)
except:
    print("ERRO -> Não foi possível se conectar ao Dobot na porta específicada.")
    # exit()

print("--------------------------------------------------")
print("Dobot conectado! Iniciando servidor")

# rota que recebe as coordenadas desejadas e movimenta o robô
@app.post("/movement")
def coordinates():
    (x, y, z, r, j1, j2, j3, j4) = request.form
    return 200

# rota que retorna as coordenadas da posição atual do robo
@app.post("/position")
def position():
    try:
        (x, y, z, r, j1, j2, j3, j4) = dobot.pose()
        return {x,y,z,j1,j2,j3,j4}, 200

    except Exception as e:
        return e, 500
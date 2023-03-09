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

@app.get("/")
def hello_world():
    return "<p>Hello, World!</p>"
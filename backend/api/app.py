from flask import Flask, request, jsonify, make_response
from controller import Controller
from serial.tools import list_ports
from prisma import Prisma, register
from prisma.models import Positions
import jsonpickle

db = Prisma()
db.connect()
register(db)


# dobot = Controller()

app = Flask(__name__)
dobotPort = "COM7"
app.config['JSON_AS_ASCII'] = False
# with connection.cursor() as cursor:
#     sql = "SELECT * FROM positions"
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     print(result)

# available_ports = list_ports.comports()
# print(f'Portas de comunicação disponíveis: {[x.device for x in available_ports]}')
# print("--------------------------------------------------")
# print(f"Conectando ao Dobot Magician Lite na porta {dobotPort}...")
# print("--------------------------------------------------")

# try:
#     dobot = Controller(dobotPort)
# except:
#     print("ERRO -> Não foi possível se conectar ao Dobot na porta específicada.")
#     # exit()

# print("--------------------------------------------------")
# print("Dobot conectado! Iniciando servidor")

# INSERE A POSIÇÃO ATUAL DO ROBO NO BANCO DE DADOS
@app.get("/getLastPositions")
def teste():
    Positions.prisma().create(data={"j1": 45,"j2":45,"j3":45})
    tee = Positions.prisma().find_many(take=3, order={"id": "desc"})
    data = []
    for i in tee: data.append(i.__dict__)
    resp = make_response("okok")
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
    # return "okok", 200

@app.post("/move")
def move():

    id = int(request.json["id"])

    if not id:
        return "nothing provided", 400
    
    data = Positions.prisma().find_unique(where={"id": id})
    return jsonify(data.__dict__), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
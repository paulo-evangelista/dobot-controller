from flask import Flask, request, jsonify, make_response
from controller import Controller
from serial.tools import list_ports
from prisma import Prisma, register
from prisma.models import Positions
import pydobot

db = Prisma()
db.connect()
register(db)
app = Flask(__name__)

dobotPort = "COM7"
available_ports = list_ports.comports()
print(f'Portas de comunicação disponíveis: {[x.device for x in available_ports]}')
print("--------------------------------------------------")
print(f"Conectando ao Dobot Magician Lite na porta {dobotPort}...")
print("--------------------------------------------------")
dobot = pydobot.Dobot(port=dobotPort, verbose=True)


@app.get("/getLastPositions")
def teste():

    positions = dobot.pose()

    Positions.prisma().create(data={"j1": positions["j1"],"j2":positions["j2"],"j3":["j3"]})
    query_data = Positions.prisma().find_many(take=3, order={"id": "desc"})
    result = []

    for i in query_data: result.append(i.__dict__)

    return jsonify(result), 200

@app.post("/move")

def move():

    id = int(request.json["id"])

    if not id:
        return "nothing provided", 400
    
    data = Positions.prisma().find_unique(where={"id": id})
    return jsonify(data.__dict__), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
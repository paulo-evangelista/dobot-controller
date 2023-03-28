from flask import Flask, request, jsonify, make_response
from serial.tools import list_ports
import PySimpleGUI as sg
from prisma import Prisma, register
from prisma.models import Positions
import pydobot
import json

db = Prisma()
db.connect()
register(db)
app = Flask(__name__)



# available_ports = list_ports.comports()
# print(f'Portas de comunicação disponíveis: {[x.device for x in available_ports]}')
dobotPort = "COM3"



# sg.theme('SystemDefault')
# layout = [  [sg.Text('Selecione a porta de comunicação do Dobot:')],
#             [sg.Text('Portas disponiveis:'), sg.Combo(values=[x.device for x in available_ports])],
#             [sg.Button('Ok')]]

# # Create the Window
# window = sg.Window('Bem vindo', layout)
# # Event Loop to process "events" and get the "values" of the inputs
# while True:
#     event, values = window.read()
#     print('You entered ', values[0])
#     if event == sg.WIN_CLOSED or event == 'Ok': # if user closes window or clicks cancel
#         dobotPort = values[0]
#         break

# window.close()

try:
    dobot = pydobot.Dobot(port=dobotPort, verbose=True)
except:
    sg.popup('Erro ao conectar com o Dobot. Verifique se a porta selecionada está correta e se o Dobot está ligado.', title='Erro')
    exit()
# grava a posição atual do dobot no banco de dados e retorna os 3 últimos registros
@app.get("/getLastPositions")
def teste():

    # pega as posições atuais do dobot
    dobot_positions = dobot.pose()

    #insere j1, j2 e j3 no banco de dados
    Positions.prisma().create(data={"j1":dobot_positions[4],"j2":dobot_positions[5],"j3":dobot_positions[6]})
    print("inserted ",dobot_positions[4],dobot_positions[5],dobot_positions[6], "  to DB.")

    # pega os 3 registros mais recentes do banco de dados
    query_data = Positions.prisma().find_many(take=3, order={"id": "desc"})

    # Os regitros são retornados como um arr de objetos, então é necessário transformar
    # em um arr de dicionários para então podermos serializar um json
    result = []
    for i in query_data: result.append(i.__dict__)

    # retorna o json
    return jsonify(result), 200

#repete as ultimas posições gravadas no banco de dados
@app.get("/repeatLastPositions")
def repeat():

    query_data = Positions.prisma().find_many(take=3, order={"id": "desc"})

    result = []
    for i in query_data: result.append(i.__dict__)

    for i in query_data:
        dobot._set_ptp_cmd(
            x=i.j1,
            y=i.j2,
            z=i.j3,
            r=4,
            wait=True,
            mode=pydobot.enums.PTPMode.MOVJ_ANGLE
            )
        
    return "ok", 200

#rota que recebe um id, busca no banco de dados e move o dobot para a posição correspondente
@app.post("/move")
def move():

    # pega o json recebido e transforma em dicionário
    received = json.loads(request.data.decode("utf-8"))

    # confere se o json recebido não está vazio
    if not received: return "nothing provided", 400

    # pega separa o id do dicionario
    id = received["id"]

    # confere se o id não é vazio
    if not id: return "nothing provided", 400
    
    # busca no banco de dados a posição correspondente ao id recebido
    data = Positions.prisma().find_unique(where={"id": id})

    # Transforma o objeto retornado pelo db em um dicionário
    positions_dict = data.__dict__

    # move o dobot para a posição correspondente
    dobot.pose()
    dobot._set_ptp_cmd(
        x=positions_dict["j1"],
        y=positions_dict["j2"],
        z=positions_dict["j3"],
        r=4,
        wait=True,
        mode=pydobot.enums.PTPMode.MOVJ_ANGLE
        )
    # retorna status de success
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True,use_reloader=False)
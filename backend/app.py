from flask import Flask, request, jsonify
from controller import Controller
from serial.tools import list_ports
import pymysql


# dobot = Controller()

app = Flask(__name__)
dobotPort = "COM7"

print("--------------------------------------------------")
print("Servidor iniciando...")
print("--------------------------------------------------")
print("Testando conexão com banco de dados...")
print("--------------------------------------------------")
try:
    connection = pymysql.connect(
        host='db',
        port=3306,
        user='user',
        password='password',
        database='db',
        )
    aa = connection.open    
    print(aa)
except Exception as e:
    print("ERRO -> Não foi possível se conectar ao banco de dados.\n",e)
    exit()


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
@app.get("/insertCurrentPosition")
def insert():
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO positions (x, y, z, r, j1, j2, j3, j4) VALUES (20,20,20,20,20,20,20,20)"
            cursor.execute(sql); cursor.fetchall()
        return "OK", 200
    
    except Exception as e:
        return e, 500

# RETORNA A POSICAO ATUAL DO ROBO
@app.get("/position")
def position():
    try:
        (x, y, z, r, j1, j2, j3, j4) = dobot.pose()
        return {x,y,z,j1,j2,j3,j4}, 200

    except Exception as e:
        return e, 500
    
# RETORNA AS 3 ULTIMAS POSIÇÕES GUARDADAS NO BANCO DE DADOS
@app.get("/getLastPositions")
def lastPositions():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM positions ORDER BY id DESC LIMIT 3"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
            return jsonify(result), 200
        
    except Exception as e:
        return e, 500



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
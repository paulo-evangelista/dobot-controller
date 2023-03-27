#criamos uma classe chamada Controller para fazer a comunicação com o Dobot
class Controller(object):
    def __init__(self, dobotPort):
        #importa as bibliotecas necessárias
            from serial.tools import list_ports

            import pydobot

            port = dobotPort

            #cria o objeto do Dobot, estabelecendo a comunicação
            self.device = pydobot.Dobot(port=port, verbose=False)
             #move o Dobot para a posição inicial
            self.device.move_to(225.7625732421875, 0.0, 150.50729370117188, 0.0, wait=True)
    
    #função para fazer o quadrado
    def square(self,l: float) :
        
        try:
            
            #posição inicial do Dobot
            (x, y, z, r, j1, j2, j3, j4) = self.device.pose()

            #move o Bobot em um quadrado
            self.device.move_to(x,y+l,z,r,wait = True)
            self.device.move_to(x+l,y+l,z,r,wait = True)
            self.device.move_to(x+l,y,z,r,wait = True)
            self.device.move_to(x,y,z,r,wait = True)
            
            return "success"
        #caso ocorra algum erro, retorna a mensagem de erro
        except Exception as e:
            return str(e)

    #função para mover o Dobot para baixo
    def down(self,value: float):
            
            try:
            
                #pega a posição atual do Dobot
                (x, y, z, r, j1, j2, j3, j4) =self.device.pose()
                #move o Dobot para baixo
                self.device.move_to(x, y, z-value,r, wait=True)
                
                return "success"

            #caso ocorra algum erro, retorna a mensagem de erro
            except Exception as e:
                return str(e)

    #função para mover o Dobot para cima
    def up(self,value: float):
        
            try:
            
                #pega a posição atual do Dobot
                (x, y, z, r, j1, j2, j3, j4) =self.device.pose()
                #move o Dobot para cima
                self.device.move_to(x, y, z+value,r, wait=True)
                
                return "success"
                #caso ocorra algum erro, retorna a mensagem de erro
            except Exception as e:
                return str(e)
            
            #função para mover o Dobot para a esquerda
    def line(self,l: float):
            try:
            
                #pega a posição atual do Dobot
                (x, y, z, r, j1, j2, j3, j4) =self.device.pose()
                #move o Dobot em uma linha
                self.device.move_to(x+l, y, z,r, wait=True)
                self.device.move_to(x-l, y, z,r, wait=True)
                
                return "success"

            except Exception as e:
                return str(e)
            
    def rotate(self,l: float):
        try:
            #pega a posição atual do Dobot
            (x, y, z, r, j1, j2, j3, j4) =self.device.pose()
            
            #rotaciona o Dobot
            self.device.move_to(x+l, y, z,r+l, wait=True)
            self.device.move_to(x-l, y, z,r-l, wait=True)
            self.device.move_to(x, y, z,r, wait=True)
                
            return "success"

        except Exception as e:
            return str(e)

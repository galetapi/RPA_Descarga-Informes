import json
from turtle import delay
import requests
import socket
from datetime import datetime
from random import randint


class log():
#metodo inicializar
    def __init__(self):
        self.fecha=''
        self.fechainicio=''
        self.ambiente='DEV'
        self.ip=socket.gethostbyname(socket.gethostname()) # nombre del portatil o pc
        self.usuario=socket.gethostname()
        self.tecnologia='SAP_SCRIPTING'
        self.proceso='Compras'
        self.proyecto='Descarga de Informes'
        self.level=''
        self.procesointerno=''
        self.mensaje=''
        self.fintransaccion=''
        self.idtransaccion=''
        self.duracion=''


    def post(self):
                
        rn=randint(10000, 99999)    
        self.idtransaccion = datetime.now().strftime("%H%M%S-")+str(rn)    
        headers = {'Content-type': 'application/json','Authorization': 'Basic ZWxhc3RpYzpKTkFuOURBc1VObjMxOU5uRVpabDFneEI='
        }
        url = "https://linea-directa.es.us-east-1.aws.found.io:9243/automatizacion/_doc/"
        data = {
                'fecha': datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000-0500"),
                'ambiente': self.ambiente,
                'ip': self.ip,
                'usuario': self.usuario,
                'tecnologia': self.tecnologia,
                'proceso': self.proceso,
                'proyecto': self.proyecto,
                'level': self.level,
                'procesointerno': self.procesointerno,
                'mensaje': self.mensaje,
                'idtransaccion': self.idtransaccion
                }
        
        postRequest = requests.post(url, data=json.dumps(data), headers=headers)
        print(postRequest.text)

    def postFin(self):

        self.duracion = self.fintransaccion - self.fechainicio 
        self.duracion = int(self.duracion.total_seconds()) 
        rn = randint(10000, 99999)    
        self.idtransaccion=datetime.now().strftime("%H%M%S-")+str(rn)    
        headers = {'Content-type': 'application/json','Authorization': 'Basic ZWxhc3RpYzpKTkFuOURBc1VObjMxOU5uRVpabDFneEI='
        }
        url = "https://linea-directa.es.us-east-1.aws.found.io:9243/automatizacion/_doc/"
        data = {
                'fecha': self.fechainicio.strftime("%Y-%m-%dT%H:%M:%S.000-0500"),
                'ambiente': self.ambiente,
                'ip': self.ip,
                'usuario': self.usuario,
                'tecnologia': self.tecnologia,
                'proceso': self.proceso,
                'proyecto': self.proyecto,
                'level': self.level,
                'procesointerno': self.ProcesoInterno,
                'mensaje': self.mensaje,
                'idtransaccion': self.idtransaccion,
                'duracion': self.duracion,
                'fintransaccion':self.fintransaccion.strftime("%Y-%m-%dT%H:%M:%S.000-0500")
                }
        
        postRequest = requests.post(url, data=json.dumps(data), headers=headers)
        print(postRequest.text)
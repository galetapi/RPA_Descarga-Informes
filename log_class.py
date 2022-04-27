import json
from turtle import delay
import requests
import socket
from datetime import datetime
from random import randint


class log():
#metodo inicializar
    def __init__(self):
        self.Fecha=''
        self.FechaInicio=''
        self.Ambiente='DEV'
        self.Ip=socket.gethostbyname(socket.gethostname()) # nombre del portatil o pc
        self.Usuario=socket.gethostname()
        self.Tecnologia='SAP_SCRIPTING'
        self.Proceso='Compras'
        self.Proyecto='Descarga de Informes'
        self.Level=''
        self.ProcesoInterno=''
        self.Mensaje=''
        self.FinTransaccion=''
        self.Idtransaccion=''
        self.Duracion=''


    def post(self):
                
        rn=randint(10000, 99999)    
        self.Idtransaccion=datetime.now().strftime("%H:%M:%S-")+str(rn)    
        headers = {'Content-type': 'application/json','Authorization': 'Basic ZWxhc3RpYzpKTkFuOURBc1VObjMxOU5uRVpabDFneEI='
        }
        url = "https://linea-directa.es.us-east-1.aws.found.io:9243/automatizacion/_doc/"
        data = {
                'Fecha': datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000-0500"),
                'Ambiente': self.Ambiente,
                'Ip': self.Ip,
                'Usuario': self.Usuario,
                'Tecnologia': self.Tecnologia,
                'Proceso': self.Proceso,
                'Proyecto': self.Proyecto,
                'Level': self.Level,
                'ProcesoInterno': self.ProcesoInterno,
                'Mensaje': self.Mensaje,
                'Idtransaccion': self.Idtransaccion
                }
        
        postRequest = requests.post(url, data=json.dumps(data), headers=headers)
        print(postRequest.text)

    def postFin(self):

        self.Duracion = self.FinTransaccion - self.FechaInicio 
        self.Duracion = int(self.Duracion.total_seconds()) 
        rn=randint(10000, 99999)    
        self.Idtransaccion=datetime.now().strftime("%H:%M:%S-")+str(rn)    
        headers = {'Content-type': 'application/json','Authorization': 'Basic ZWxhc3RpYzpKTkFuOURBc1VObjMxOU5uRVpabDFneEI='
        }
        url = "https://linea-directa.es.us-east-1.aws.found.io:9243/automatizacion/_doc/"
        data = {
                'Fecha': self.FechaInicio.strftime("%Y-%m-%dT%H:%M:%S.000-0500"),
                'Ambiente': self.Ambiente,
                'Ip': self.Ip,
                'Usuario': self.Usuario,
                'Tecnologia': self.Tecnologia,
                'Proceso': self.Proceso,
                'Proyecto': self.Proyecto,
                'Level': self.Level,
                'ProcesoInterno': self.ProcesoInterno,
                'Mensaje': self.Mensaje,
                'Idtransaccion': self.Idtransaccion,
                'Duracion': self.Duracion,
                'FinTransaccion':self.FinTransaccion.strftime("%Y-%m-%dT%H:%M:%S.000-0500")
                }
        
        postRequest = requests.post(url, data=json.dumps(data), headers=headers)
        print(postRequest.text)
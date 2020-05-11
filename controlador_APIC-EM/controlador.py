# El usuario tendrá que escoger la opción que quiera (no tendrá que especificar la url a mano)
# Añadir, como mínimo, 4 funcionalidades
import requests
import json
import urllib3
from pprint import pprint

requests.packages.urllib3.disable_warnings()
url_base = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/"


def menu():
   print("**********************")
   print("Introduce la operacion")
   print("1 lista de dispositivos ")
   print("2 Informacion host")
   print("3 Informacion de interface")
   print("4 ")
   print("**********************")
   return input("")



#Obtenemos el ticket
def getTicket():
   url = url_base + "ticket"
   headers = {
      'Content-Type' : 'application/json'
   }
   body_json = {
      "password" : "Xj3BDqbU",
      "username" : "devnetuser"
   }
   resp = requests.post(url,json.dumps(body_json),headers=headers,verify=False) 
   #print("La peticion tiene el estado:",resp.status_code)
   response_json = resp.json()
   serviceTicket = response_json["response"]["serviceTicket"]
   return serviceTicket

def get_device():
   url = url_base + "network-device"
   serviceTicket = getTicket() #Por si hay mucha espera entre una peticion y otra que siempre lo pida
   headers = {
      'Content-Type' : 'application/json',
      "X-Auth-Token" : serviceTicket
   }
   resp = requests.get(url,headers=headers,verify=False) 
   response_json = resp.json()
   #for device in response_json["response"]:
   for device in response_json['response']:
       print("hostname",device['hostname'],"familia",device["family"],"su Mac",device["macAddress"],"version",device["softwareVersion"])


def get_host():
   url = url_base + "host"
   serviceTicket = getTicket() #Por si hay mucha espera entre una peticion y otra que siempre lo pida
   headers = {
      'Content-Type' : 'application/json',
      "X-Auth-Token" : serviceTicket
   }
   resp = requests.get(url,headers=headers,verify=False) 
   response_json = resp.json()
   #for device in response_json["response"]:
   for device in response_json['response']:
       print("ip ",device['hostIp'],"   tipo",device["hostType"],"   direccion Mac",device["hostMac"])
  

def get_interface():
   url = url_base + "interface"
   serviceTicket = getTicket() #Por si hay mucha espera entre una peticion y otra que siempre lo pida
   headers = {
      'Content-Type' : 'application/json',
      "X-Auth-Token" : serviceTicket
   }
   resp = requests.get(url,headers=headers,verify=False) 
   response_json = resp.json()
   #for device in response_json["response"]:
   for device in response_json['response']:
       print("NombreClase ",device['className'],"   estado",device["status"],"   tipo de interfaz",device["interfaceType"])

def get_generico(direccion="interface",item1="className",item2="status",item3="interfaceType"):
   print(direccion,item1,item2,item3)
   url = url_base + direccion
   serviceTicket = getTicket() #Por si hay mucha espera entre una peticion y otra que siempre lo pida
   headers = {
      'Content-Type' : 'application/json',
      "X-Auth-Token" : serviceTicket
   }
   resp = requests.get(url,headers=headers,verify=False) 
   response_json = resp.json()
   for device in response_json['response']:
       print(item1,"=",device[item1],"\n",item2,"=",device[item2],"\n",item3,"=",device[item3],"\n")

#pregunta al usuario la direccion a conectarse y sus posibles atributos
def generico():
   get_generico(input("direccion "),input("item1 "),input("item2 "),input("item3 "))

def opcion(opcion):
   if (opcion == "1"):
      get_device()
   elif(opcion == "2"):
      get_host()
   elif(opcion == "3"):
      get_interface()
   elif(opcion == "4"):
      generico()
   else:
      print("opcion no valida")

if __name__ == "__main__":
   opcion(menu())
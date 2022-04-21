
from operator import le
from re import T
from firebase import firebase
import tkinter as tk
from tkinter import filedialog
import asyncio
import requests

import pandas as pd
URL = 'https://www.api.carlostapiad.com/api/prospectos' 
raiz=tk.Tk()
raiz.geometry('300x200')
estado=tk.StringVar()
estado.set("desactivado")
raiz.title("Carlos Tapia D")
archivo=''
def changeText(value):
    estado.set(value)

def seleccionarArchivo():
       
    
    archivo=filedialog.askopenfilename(title="Abrir",initialdir="C:/")
    leerExcel(archivo)
    
    
def leerExcel(ruta):
    # try:
        lecturaf = pd.read_excel(ruta)
        
    
        for i in lecturaf.index: 
            # prisnt("se guardo")
            # print("los campos"+ lecturaf["Nombre"][i]+ ","+str(lecturaf["URL LinkedIn"][i]+","+lecturaf["Puesto"][i]+","+str(lecturaf["Número"][i])+""+lecturaf["Correo"][i]))
            # fireread=firebase.FirebaseApplication("https://prueba-tecnica-d5940-default-rtdb.firebaseio.com/",None)
            headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
}
            data2 = requests.get(URL+"/"+lecturaf["Nombre"][i],headers=headers) 
            data2 = data2.json()
   
            if data2==[] :
                
                datos={'name':lecturaf["Nombre"][i],
                    'linkedin':str(lecturaf["URL LinkedIn"][i]),
                    'puesto':lecturaf["Puesto"][i],
                    'numero':str(lecturaf["Número"][i]),
                    'email':lecturaf["Correo"][i]}
                subirdatos(datos)
                changeText('Activo')
            else :
                for element in data2: #iteramos sobre data
                    datos={'name':lecturaf["Nombre"][i],
                    'linkedin':str(lecturaf["URL LinkedIn"][i]),
                    'puesto':lecturaf["Puesto"][i],
                    'numero':str(lecturaf["Número"][i]),
                    'email':lecturaf["Correo"][i],
                    'id':element["id"]}
                    actualizar(datos)
        changeText('conectado')
                    
                   
                
            # lectura=fireread.get("/prospectos",None,params={'Nombre':lecturaf["Nombre"][i]})
            # databse=list(lectura.values())
            # databse=lecturax.difference()
            # print(databse)
            # if lectura['Nombre'][0] == lecturaf["Nombre"][i] :
            #     print("se actualizo")
            # else:
            #     print("se guardo")
            # print("lectura")
            # print(lectura)
           
    # except:
        # changeText('El archivo debe se una extencion de xlsx y debe tener un formato especifico ')

def subirdatos(datos):
    # print(datos)
    
    # try:
        changeText('conectando...')
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}    
        response =requests.post(URL, json= datos,headers=headers)
        print('se guardo')
        changeText('conectado')
    # except:
        # changeText('el archivo no se pudo sincronizar revisa que tengas internet')
        
        
def actualizar(datos):
    
    try:
        changeText('conectando...')
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}    
        
        response =requests.put(URL+"/update", data= datos,headers=headers)
        print("se actualizo")
        changeText('conectado')
        
    except:
        changeText('el archivo no se pudo sincronizar revisa que tengas internet')
        


tk.Label(raiz,text="Selecciona el archivo a vincular a la nube").pack()
    
tk.Button(raiz,text="Seleccionar ruta",command=seleccionarArchivo).pack()

tk.Label(raiz,textvariable=estado).pack()

raiz.mainloop()
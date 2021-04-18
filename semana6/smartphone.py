'''
Nombre: Jonathan Granillo Robledo
Grupo: 21
Fecha:25/02/2021
Descripción: la computadora aprendera a diferenciar entre un iphone 12 y un samsung s21 ultra
'''
import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def clasificar(text):
    key = "5fc46df0-77a5-11eb-8833-91913a1fc472d7dfcd06-a6e3-494b-a7b3-7a3c6f1009c6"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

while True:
    pregunta = input("ingrese las carcateristicas del smarphone : ")
 # CHANGE THIS to something you want your  machine learning model to classify
    demo = clasificar(pregunta)

    label = demo["class_name"]
    confidence = demo["confidence"]

    if label == "samsung_s21_ultra":
        print("te envio el Samsung s21 ultra")
    elif label == "iphone_12":
        print("te envio el iphone 12")
        

'''
Nombre: Jonathan Granillo Robledo
Grupo: 21
Fecha:17/04/2021
Descripción: este codigó sera mi complemento para mi proyecto de bot que se esta realizando
'''
import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "f2d722a0-a008-11eb-af6c-0d26e5364484fb1756f8-960f-48b2-a97d-f7fe46998972"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

# CHANGE THIS to something you want your machine learning model to classify
for i in range(3):
    texto = input("Dame un texto:")
    demo = classify(texto)

    label = demo["class_name"]
    confidence = demo["confidence"]

    if label == "Saludo":
        print("Bienvenido")
    else:
        print("hasta luego")




    
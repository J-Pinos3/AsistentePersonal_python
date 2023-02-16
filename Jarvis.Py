import speech_recognition as sr
import webbrowser#por defecto pertenece a python
import pyttsx3
import pywhatkit
import urllib.request
import json
from datetime import datetime
import wikipedia

name = "cortana"
key = "AIzaSyBPyCeyEu5E5keMf3u3IICfCxmkB6DwlIY"

listener = sr.Recognizer()
engine = pyttsx3.init()#se inicializa el paquete
voices = engine.getProperty("voices")#obener listado de voces disponibles
engine.setProperty("voice", voices[0].id)#elegir una voz

def talk(text):
    engine.say(text)
    engine.runAndWait()



def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)#escucha la info de la fuente <source>
            rec = listener.recognize_google(voice)
            rec = rec.lower()#todo a minusculas
            if name in rec:#elimina el nombre del asistente y muestra el mensaje
                rec = rec.replace(name,"")
                #talk(rec)
                print(rec)
    except:
        pass
    return rec
    #devolvemos la cadena con lo que hablamos


def run():
    rec = listen() #almacena una lista con lo antes dicho
    if "reproduce" in  rec:#si en la oración hay reproduce, abrirá Yt
        music = rec.replace("reproduce","")
        talk("Reproduciendo " + music)
        pywhatkit.playonyt(music)


    if "hora" in rec:
        #hora = datetime.now().strftime("%I:%M %p")
        hora = datetime.now().strftime("%H:%M %S")
        talk("Son las " + hora)


    if "busca" in rec:
        order = rec.replace("busca","")
        info = wikipedia.summary(order,1)
        talk(info)

    if "amazon" in rec:
        webbrowser.open("https://amazon.com")

run()



#

#

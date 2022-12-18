import speech_recognition as sr
import webbrowser#por defecto pertenece a python
import pyttsx3
import pywhatkit
import urllib.request
import json
import datetime
import wikipedia

name = "jarvis"
key = "AIzaSyCty8voJPe3YqveBfbvujP0m-eLzIMc6v0"

listener = sr.Recognizer()
engine = pyttsx3.init()#se inicializa el paquete
voices = engine.getProperty("voices")#obener listado de voces disponibles
engine.setProperty("voice", voices[1].id)#elegir una voz

def talk(text):
    engine.say(text)
    engine.runAndWait()



def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)#escucha la info de la fuente <source>
            rec = listener.recognize_google(voice,languaje="es-Es")#con la api de google almacena lo escuchado en una lista string
            rec = rec.lower()#todo a minusculas
            if name in rec:#elimina el nombre del asistente y muestra el mensaje
                rec = rec.replace(name,"")
                #talk(rec)
                print(rec)
    except:
        pass
    return rec#devolvemos la cadena con lo que hablamos


def run():
    rec = listen() #almacena una lista con lo antes dicho
    if "reproduce" in  rec:#si en la oración hay reproduce, abrirá Yt
        music = rec.replace("reproduce","")
        talk("Reproduciendo " + music)
        pywhatkit.playonyt(music)

    #cuantos suscriptores tiene x youtuber
    if "cuantos suscriptores tiene" in rec:
        name_subs = rec.replace("cuantos suscriptores tiene","")
        data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+name_subs.strip()+'&key='+key).read()
        subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
        talk(name_subs + " tiene {:,d}".format(int(subs)) +" suscriptores ")

    if "hora" in rec:
        hora = datetime.datetime().now().strftime("%I:%M %p")
        talk("Son las " + hora)

    if "busca" in rec:
        order = rec.replace("busca","")
        info = wikipedia.summary(order,1)
        talk(info)

run()



#

#

import speech_recognition as sr 
import pyttsx3
import pywhatkit
import urllib.request
import json 
import datetime
import wikipedia
from googletrans import Translator


listener =sr.Recognizer()
engine = pyttsx3.init()
translator = Translator()
name = 'pedro'
# obtenes el arreglo con las diferentes voces y seteamos con la ide del la voz en el arreglo 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# funcion base para que hable el engine 
def talk(text):
    engine.say(text)
    engine.runAndWait()
# funcion de se activa el microfono y se setean los parametro de escucha donde name representa
# el nombre de activacion para los comandos y rec el la variable que almacena lo que se dijo 
def escucha():
    try:
        with sr.Microphone() as source:
            print("Escuchando....")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice)
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
                #print(rec)
                
    except:
        pass
    return rec

# aqui en piezan las funciones especializadas 

#funcion para buscar en youtube con la libreria pywhatkit 
def run():
    rec = escucha()
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        talk('Reproduciendo'+ music)
        pywhatkit.playonyt(music)
    
    elif 'hora' in rec:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk("Son las"+hora)
    elif 'busca' in rec:
        order = rec.replace('busca', '')
        info = wikipedia.set_lang('es'),wikipedia.summary(order, 1)
        print(info)
        talk (info)


run()
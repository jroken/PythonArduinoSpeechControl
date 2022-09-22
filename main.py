from serial import Serial 
from time import sleep
from gtts import gTTS
import speech_recognition as spr
import os
import random
from playsound import playsound

ArduinoSerial = Serial('com6',9600)

sleep(2)

def speak(string):
    tts = gTTS(text=string, lang='tr', slow=False)
    rand = random.randint(1, 30)
    sayi = 1 + rand
    file = f"answer{sayi}.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

speak('Günaydın Efendim')
print(ArduinoSerial.readline())

while True:
    r = spr.Recognizer()
    with spr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening:" + str(r.energy_threshold))
        voice = r.listen(source)
        veri = r.recognize_google(voice, language='tr-Tr', show_all=False)
        print(r.recognize_google(voice, language='tr-Tr', show_all=False))

    if (veri == 'Selam'):
        speak('Açıyorum canım')
        ArduinoSerial.write(b'g')
        

    if (veri == 'mavi Işıkları aç'):
        ArduinoSerial.write(b'b')
        speak('Open The All Blue Light') ## Mavi ışıkları Açar 
        ## aşağıya doğru istediğiniz komutları ekleyebilirsiniz iyi çalışmalar

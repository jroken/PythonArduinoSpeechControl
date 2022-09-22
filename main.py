from serial import Serial 
from time import sleep
import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init("sapi5")
engine.setProperty('rate', 130)
ArduinoSerial = Serial('com6',9600)
sleep(2)
def speak(text):
    speak(text) 
speak('Günaydın Efendim')
print(ArduinoSerial.readline())
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Arka plan gürültüsü:" + str(r.energy_threshold))
        ses = r.listen(source, timeout=10, phrase_time_limit=10)
        veri = r.recognize_google(ses, language='tr-tr')
        print(veri)
        
    if (veri == 'yeşil Işıkları aç'):
        ArduinoSerial.write(b'g')
        speak('Open The All Green Light')

    if (veri == 'mavi Işıkları aç'):
        ArduinoSerial.write(b'b')
        speak('Open The All Blue Light') ## Mavi ışıkları Açar 
        ## aşağıya doğru istediğiniz komutları ekleyebilirsiniz iyi çalışmalar

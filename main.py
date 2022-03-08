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
        speak('Open The All Blue Light')

    if (veri == 'mavi1 aç'):
        ArduinoSerial.write(b'1')
        speak('Number One Blue Light Turned On')


    if (veri == 'mavi2 aç'):
        ArduinoSerial.write(b'2')
        speak('Number Two Blue Light Turned On')


    if (veri == 'mavi3 aç'):
        ArduinoSerial.write(b'3')
        speak('Number Tree Blue Light Turned On')


    if (veri == 'yesil1 aç'):
        ArduinoSerial.write(b'4')
        speak('Number One Green Light Turned On')


    if (veri == 'yesil2 aç'):
        ArduinoSerial.write(b'5')
        speak('Number Two Green Light Turned On')


    if (veri == 'yesil3 aç'):
        ArduinoSerial.write(b'6')
        speak('Number Tree Green Light Turned On')


    if (veri == 'yesil4 aç'):
        ArduinoSerial.write(b'7')
        speak('Number Four Green Light Turned On')


    if (veri == 'mavi bir aç'):
        ArduinoSerial.write(b'1')
        speak('Number One Blue Light Turned On')


    if (veri == 'mavi iki aç'):
        ArduinoSerial.write(b'2')
        speak('Number Two Blue Light Turned On')


    if (veri == 'mavi üç aç'):
        ArduinoSerial.write(b'3')
        speak('Number Tree Blue Light Turned On')


    if (veri == 'yesil bir aç'):
        ArduinoSerial.write(b'4')
        speak('Number One Green Light Turned On')


    if (veri == 'yesil iki'):
        ArduinoSerial.write(b'5')
        speak('Number Two Green Light Turned On')


    if (veri == 'yesil üç aç'):
        ArduinoSerial.write(b'6')
        speak('Number Tree Green Light Turned On')


    if (veri == 'yesil dört aç'):
        ArduinoSerial.write(b'7')
        speak('Number Four Green Light Turned On')



    if (veri == 'mavi 1 aç'):
        ArduinoSerial.write(b'1')
        speak('Number One Blue Light Turned On')


    if (veri == 'mavi 2 aç'):
        ArduinoSerial.write(b'2')
        speak('Number Two Blue Light Turned On')


    if (veri == 'mavi 3 aç'):
        ArduinoSerial.write(b'3')
        speak('Number Tree Blue Light Turned On')


    if (veri == 'yesil 1 aç'):
        ArduinoSerial.write(b'4')
        speak('Number One Green Light Turned On')


    if (veri == 'yeşil 2 aç'):
        ArduinoSerial.write(b'5')
        speak('Number Two Green Light Turned On')


    if (veri == 'yeşil 3 aç'):
        ArduinoSerial.write(b'6')
        speak('Number Tree Green Light Turned On')


    if (veri == 'yesil 4 aç'):
        ArduinoSerial.write(b'7')
        speak('Number Four Green Light Turned On')

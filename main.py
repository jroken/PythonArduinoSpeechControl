from serial import Serial 
import time
import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init("sapi5")
engine.setProperty('rate', 130)
ArduinoSerial = Serial('com6',9600)
time.sleep(2)
def speak():
    engine.say('')
    pass
engine.say('Günaydın Efendim')
engine.runAndWait()
print(ArduinoSerial.readline())
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Arka plan gürültüsü:" + str(r.energy_threshold))
        ses = r.listen(source, timeout=10, phrase_time_limit=10)
        print(r.recognize_google(ses, language='tr-tr'))
        veri = r.recognize_google(ses, language='tr-tr')
    if (veri == 'yeşil Işıkları aç'):
        ArduinoSerial.write(b'g')
        engine.say('Open The All Green Light')
        engine.runAndWait()
    if (veri == 'mavi Işıkları aç'):
        ArduinoSerial.write(b'b')
        engine.say('Open The All Blue Light')
        engine.runAndWait()

    if (veri == 'mavi1 aç'):
        ArduinoSerial.write(b'1')
        engine.say('Number One Blue Light Turned On')
        engine.runAndWait()

    if (veri == 'mavi2 aç'):
        ArduinoSerial.write(b'2')
        engine.say('Number Two Blue Light Turned On')
        engine.runAndWait()

    if (veri == 'mavi3 aç'):
        ArduinoSerial.write(b'3')
        engine.say('Number Tree Blue Light Turned On')
        engine.runAndWait()

    if (veri == 'yesil1 aç'):
        ArduinoSerial.write(b'4')
        engine.say('Number One Green Light Turned On')
        engine.runAndWait()

    if (veri == 'yesil2 aç'):
        ArduinoSerial.write(b'5')
        engine.say('Number Two Green Light Turned On')
        engine.runAndWait()

    if (veri == 'yesil3 aç'):
        ArduinoSerial.write(b'6')
        engine.say('Number Tree Green Light Turned On')
        engine.runAndWait()

    if (veri == 'yesil4 aç'):
        ArduinoSerial.write(b'7')
        engine.say('Number Four Green Light Turned On')
        engine.runAndWait()

    if (veri == 'mavi bir aç'):
        ArduinoSerial.write(b'1')
        engine.say('Number One Blue Light Turned On')
        engine.runAndWait()

    if (veri == 'mavi iki aç'):
        ArduinoSerial.write(b'2')
        engine.say('Number Two Blue Light Turned On')
        engine.runAndWait()

    if (veri == 'mavi üç aç'):
        ArduinoSerial.write(b'3')
        engine.say('Number Tree Blue Light Turned On')
        engine.runAndWait()

    if (veri == 'yesil bir aç'):
        ArduinoSerial.write(b'4')
        engine.say('Number One Green Light Turned On')
        engine.runAndWait()

    if (veri == 'yesil iki'):
        ArduinoSerial.write(b'5')
        engine.say('Number Two Green Light Turned On')
        engine.runAndWait()

    if (veri == 'yesil üç aç'):
        ArduinoSerial.write(b'6')
        engine.say('Number Tree Green Light Turned On')
        engine.runAndWait()

    if (veri == 'yesil dört aç'):
        ArduinoSerial.write(b'7')
        engine.say('Number Four Green Light Turned On')
        engine.runAndWait()


    if (veri == 'mavi 1 aç'):
        ArduinoSerial.write(b'1')
        engine.say('Number One Blue Light Turned On')
        engine.runAndWait()

    if (veri == 'mavi 2 aç'):
        ArduinoSerial.write(b'2')
        engine.say('Number Two Blue Light Turned On')
        engine.runAndWait()

    if (veri == 'mavi 3 aç'):
        ArduinoSerial.write(b'3')
        engine.say('Number Tree Blue Light Turned On')
        engine.runAndWait()

    if (veri == 'yesil 1 aç'):
        ArduinoSerial.write(b'4')
        engine.say('Number One Green Light Turned On')
        engine.runAndWait()

    if (veri == 'yeşil 2 aç'):
        ArduinoSerial.write(b'5')
        engine.say('Number Two Green Light Turned On')
        engine.runAndWait()

    if (veri == 'yeşil 3 aç'):
        ArduinoSerial.write(b'6')
        engine.say('Number Tree Green Light Turned On')
        engine.runAndWait()

    if (veri == 'yesil 4 aç'):
        ArduinoSerial.write(b'7')
        engine.say('Number Four Green Light Turned On')
        engine.runAndWait()
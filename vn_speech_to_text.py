import speech_recognition as sr
import pyaudio
import time
r = sr.Recognizer()
with sr.Microphone(device_index=0) as source:
    print("Mời bạn nói: ")
    sentence = ''
    while True:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio,language="vi-VI")
            sentence = sentence + " " + text
            print(sentence)
        except:
            print("Time out")
            break
#!/usr/bin/python3

import pyaudio
import speech_recognition as sr


myPyAudio = pyaudio.PyAudio()
print("Seeing pyaudio devices:",myPyAudio.get_device_count())
index = myPyAudio.get_device_count() - 1
print(index)

r = sr.Recognizer()

with sr.Microphone(index) as source: 
    audio = r.listen(source) 

try:
    print("You said " + r.recognize(audio))   
except LookupError:                           
    print("Could not understand audio")

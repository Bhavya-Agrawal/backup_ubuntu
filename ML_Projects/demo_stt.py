#!/usr/bin/python3

import speech_recognition as sr
#import pyaudio
#import os

#give audio input to computer via recorded audio file
r = sr.Recognizer()
audio = sr.AudioFile("hello.wav")
with audio as source:
	r.adjust_for_ambient_noise(source,duration=0.5)
	audio_get = r.listen(source)


text=r.recognize_google(audio_get)
print("The text is : ",text)
	


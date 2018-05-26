#!/usr/bin/python3
from gtts import gTTS
import os
string =input("enter something")
#tts = gTTS(text="hello",lang="en")

#call the linux command in backgroung of the input string
os.system(string)

os.system(string+"festival --tts")
tts = gTTS(text=string,lang="en")
# to save audio file in hello.mp3 at the same location as that of this file
tts.save("hello.mp3")
# starting the audio file using mpg321 driver
os.system("mpg321 hello.mp3")

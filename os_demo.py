
#!/usr/bin/python3

import os

#os.system(espeak)
string = input("Enter something here!!!!\n")
output = os.system(string)
# os.system returns the unix value for showing success of os.system() command
print(output)

#os.system('echo %s|festival --tts' % os.system(string))
os.system(string+" | festival --tts") 

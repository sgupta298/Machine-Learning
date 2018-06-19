import speech_recognition as sr
import numpy
import matplotlib.pyplot as mp

r=sr.Recognizer()
with sr.Microphone() as source:
    print("Speak:")
    audio = r.listen(source)
try:
    s=r.recognize_google(audio)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
print(s)
print(s.split())
mp.scatter(s.split()[4],s.split()[6],label='first')
mp.plot(s.split()[5],s.split()[8],label='second')
mp.grid()
mp.legend()
mp.show()

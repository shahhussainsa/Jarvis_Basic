import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import os
import pyjokes
import time


def speechtext():
  recognizer = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening......")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)
    try:
      print("Recognizing......")
      data = recognizer.recognize_google(audio)
      return data
    except sr.UnknownValueError:
      print("Not found")
      
def speechread(x):
  engine = pyttsx3.init()
  voices = engine.getProperty("voices")
  engine.setProperty("voice",voices[0].id)
  rate = engine.getProperty("rate")
  engine.setProperty("rate", 150)
  engine.say(x)
  engine.runAndWait()

if __name__ == '__main__':
  if "hey jarvis" in speechtext().lower():
      while True:
        speechtxt = speechtext().lower()
        
        if "your name" in speechtext:
          name = "My name id Jarvis"
          speechread(name)
        elif "youtube" in speechtext:
          webbrowser.open("https://www.youtube.com/")
        elif "time" in speechtext:
          time = datetime.datetime.now().strftime("%I%M%p")
          speechread(time)   
        elif "joke" in speechtext:
          jokes = pyjokes.get_joke(language="en", category="neutral")
          print(jokes)
          speechtext(jokes)  
        elif "play song" in speechtext:
          add = "Desktop\pythonprgm"
          listsong = os.listdir(add)
          os.startfile(os.path.join(add, listsong[0]))
        elif "exit" in speechtext:
          speechread("Thank You")
          break
      time.sleep(8)
  else:
      print("thanks")
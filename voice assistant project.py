import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser
engine=pyttsx3.init()
voices=engine.getproperty('voices')
engine.setproperty('voice', voices[1].id)
recognizer=sr.Recognizer()
def cmd():
    with sr.microphone() as source:
        print('clearing background noises...please wait')
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        print(' ask me anything..')
        recordedaudio=recognizer.listen(source)
        try:
     
         command=recognizer.recognize_google('recordedaudio,language=en_US')
         text=text.lower()
         print('your message:,format(text)')
         if 'chrome' in command:
             a='opening chrome..'
             engine.say(a)
             engine.runandwait()
             program="c;\program files\google\chrome\application\chrome.exe"
             subprocess.popen([program])
         if 'time' in command:
              time=datetime.datetime.now().strftime('%I:%M %P')
              print(time)
              engine.say(time)
              engine.runandwait()
         if  'play' in command:
              b='opening youtube'
              engine.say(b)
              engine.runandwait()
              pywhatkit.playonyt(command)
         if 'youtube'in command:
             b='opening youtube'
             engine.say(b)
             engine.runandwait()
             program="c;\program files\google\chrome\application\chrome.exe"
             
             

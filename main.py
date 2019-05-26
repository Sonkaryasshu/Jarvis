import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('espeak')
engine.setProperty('voice', 'english-us')

''' VOLUME '''
voulume = engine.getProperty('volume')
print(voulume)

''' RATE '''
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour<12:
        speak("Good morning sir")
    elif hour>=12 and hour<18:
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")
    speak("this is jarvis, how may i help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as micIn:
        print("Listening...")
        audio = r.listen(micIn)
    
    try:
        print("Recognizing...")
        query = r.recognize_sphinx(audio, language='en-in')
        print(f"User : {query}\n")
    except Exception as err:
        print(err)
        print("Please say that again")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    takeCommand()
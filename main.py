import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import smtplib

engine = pyttsx3.init('sapi5')
engine.setProperty('voice', 'english-us')

''' VOLUME '''
voulume = engine.getProperty('volume')
# print(voulume)

''' RATE '''
rate = engine.getProperty('rate')   # getting details of current speaking rate
# print (rate)                        #printing current voice rate


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
        query = r.recognize_google(audio, language='en-in')
        print(f"User : {query}\n")
    except Exception as err:
        print(err)
        speak("Sorry sir! Please say that again")
        return "None"
    return query

def sendEmail(to,body):
    server = smtplib.SMTP('smtp.gmail.com',port=587)
    server.ehlo()
    server.starttls()
    server.login('myMail@gmail.com','myPass')
    body = body + '\nThis is an automatic mail from Jarvis.'
    server.sendmail('myMail@gmail.com', to, body)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            query = query.replace('wikipedia', ' ',1)
            query = wikipedia.summary(query, sentences=2)
            print(f"Wikipedia result: {query}")
            speak(query)
        elif 'time' in query:
            time = datetime.datetime.now().time().strftime('%H:%M')
            speak('Sir,the time is'+time)
        elif 'open code' in query:
            path = 'C:\\Program Files\\Microsoft VS Code\\Code.exe'
            os.startfile(path)
        elif 'open notepad' in query:
            path = "C:\WINDOWS\system32\\notepad.exe"
            os.startfile(path)
        elif 'open youtube' in query:
            webbrowser.open('www.youtube.com')
        elif 'email to kuldeep' in query:
            try:
                speak('What should i say?')
                body = takeCommand()
                to = 'kuldeepMail@gmail.com'
                sendEmail(to,body)
                speak('Email has been sent!')
            except Exception as e:
                print(e)
                speak('Sorry sir, their was a problem in sending mail. Please try again.')
        elif 'shutdown' in query:
            exit(0)
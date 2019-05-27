# Author: Yashwant Kumar Sonkar
# sonkaryasshu@gmail.com

'''
Importing important libraries
'''
import pyttsx3                   # for text to speak translation
import datetime
import speech_recognition as sr  # for speech recognition
import wikipedia
import os
import webbrowser
import smtplib                   # for sending mail

'''
Setting up pyttsx3
'''
engine = pyttsx3.init('sapi5') 
engine.setProperty('voice', 'english-us')

''' Volume '''
voulume = engine.getProperty('volume')
# print(voulume)
# engine.setProperty('volume', 1)
''' Rate '''
rate = engine.getProperty('rate')   
# print (rate)                      
# engine.setProperty('rate', 150)

def speak(audio):
    '''
    this function takes string as a parameter and speaks out that string using pyttsx3
    '''
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    '''
    this function wishes you according to the time
    '''
    hour = int(datetime.datetime.now().hour)
    if hour<12:
        speak("Good morning sir")
    elif hour>=12 and hour<18:
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")
    speak("this is jarvis, how may i help you")

def takeCommand():
    '''
    this function takes voice input from user and return a string corresponding to that input
    '''
    r = sr.Recognizer()
    with sr.Microphone() as micIn:
        print("Listening...")
        audio = r.listen(micIn)
    
    try:
        print("Recognizing...")
        # can change this recognizer to your choice
        query = r.recognize_google(audio, language='en-in')
        print(f"User : {query}\n")
    except Exception as err:
        print(err)
        speak("Sorry sir! Please say that again")
        return "None"
    return query

def sendEmail(to,body):
    '''
    send email using smtp module by taking destination email address and body of mail as parameters
    '''
    server = smtplib.SMTP('smtp.gmail.com',port=587)
    server.ehlo()
    server.starttls()
    server.login('myMail@gmail.com','myPass')
    body = body + '\nThis is an automatic mail from Jarvis.'
    server.sendmail('myMail@gmail.com', to, body)
    server.close()

if __name__ == "__main__":
    wishMe() # wishes you at startup
    while True:
        # taking voice input from user
        query = takeCommand().lower()
        # matching input query to differnt options
        # search wikipedia for the input
        if 'wikipedia' in query:
            query = query.replace('wikipedia', ' ',1)
            query = wikipedia.summary(query, sentences=2)
            print(f"Wikipedia result: {query}")
            speak(query)
        # speak current time
        elif 'time' in query:
            time = datetime.datetime.now().time().strftime('%H:%M')
            speak('Sir,the time is'+time)
        # open VS code
        elif 'open code' in query:
            path = 'C:\\Program Files\\Microsoft VS Code\\Code.exe'
            os.startfile(path)
        # open notepad
        elif 'open notepad' in query:
            path = "C:\WINDOWS\system32\\notepad.exe"
            os.startfile(path)
        # open youtube
        elif 'open youtube' in query:
            webbrowser.open('www.youtube.com')
        # send email
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
        # exit program
        elif 'shutdown' in query:
            speak('Bye sir, Hope you enjoyed my assistance')
            exit(0)
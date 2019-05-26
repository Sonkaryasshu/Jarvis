import pyttsx3

engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
# for v in voices:
#     print(v.id)
# for voice in voices:
#    engine.setProperty('voice', voice.id)
#    print(voice.id)
#    engine.say('The quick brown fox jumped over the lazy dog.')
#    engine.runAndWait()

engine.setProperty('voice', 'english-us')
v = engine.getProperty('voice')
print(v)

''' VOLUME '''
voulume = engine.getProperty('volume')
print(voulume)

''' RATE '''
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate


engine.say("Hello friends, this is jarvis")
engine.runAndWait()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == "__main__":
    speak('hello brother')
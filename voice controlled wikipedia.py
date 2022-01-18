import wikipedia
import pyttsx3
import speech_recognition as sr
import playsound
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)       # 0 represents the male voice, if you need female voice means just type 1 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("hey buddy")
while True:
    speak("what do you want from wikipedia")
    try:
        r=sr.Recognizer()
        with sr.Microphone() as source:
            playsound.playsound("D:\\Python\\ironmanjarvis\\Music\\start.mp3")      # This is just a sound to verify the mic is on
            print("Listening...")
            r.pause_threshold=1
            r.adjust_for_ambient_noise(source)
            audio=r.listen(source)
            playsound.playsound("D:\\Python\\ironmanjarvis\\Music\\stop.mp3")        # This is just a sound to verify the mic is off
            print("Recognizing...")
            search=r.recognize_google(audio,language='en-in')
            print("user said : ",end=" ")
        speak("searching,  please wait")
        results=wikipedia.summary(search,sentences=2)
        speak("according to wikipedia")
        print(results)
        speak(results)
        speak("thats all buddy")
        print("\n\t\t\t\t\t\t--------- x ---------")
    except Exception as e:
        print(e)
        speak("say that again please")

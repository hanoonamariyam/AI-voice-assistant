import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime



def speak(text):
    engine = pyttsx3.init()
    engine.say(text)  
    engine.runAndWait()
    engine.stop()
    

#function for listenng
def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
      print("Listening...")
      r.adjust_for_ambient_noise(source,duration=1)
      audio = r.listen(source,timeout=5,phrase_time_limit=
5)
    try:
        command = r.recognize_google(audio)
        print("you said:", command) 
        return command.lower()

    except sr.UnknownValueError:
        print("could not understand")
        return ""
    except sr.RequestError:
        print("internet issue")
        return ""
    except Exception as e:
        print("Error:",e)
        return ""
#GREETING
speak("Hello, I am your assistant")

#main loop
while True:
    command = listen()

    if "youtube" in command:
        speak("Opening youtube")
        webbrowser.open("https://youtube.com")

    elif "google" in command:
        speak("Opening google")
        webbrowser.open("https://google.com")

    elif "time" in command:
        current_time =datetime.datetime.now().strftime("%I:%M %p")
        speak("Current time is" + current_time)

    elif "date" in command:
        today = datetime.datetime.now().strftime("%d %B %Y")

    elif "stop" in command:
        speak("Goodbye")
        break 
    elif command == "":
        continue
    else:
        speak("please say that again")
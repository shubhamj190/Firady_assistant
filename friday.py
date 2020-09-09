import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
# print(voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    # it takes microphone input and gives us a stgring output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print('Recognizing...')
        query=r.recognize_google(audio, language='en-in')
        print('user said : ',query)
        # speak(query)

    except Exception:
        # print(e)
        print('Please say that again...')
        return None
    return query

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning, sir!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon, sir!")
    else:
        speak("Good Evening sir!")
    
    speak('how may i help you ?')

if __name__ == "__main__":
        wishme()
        while(True):
            query =  takeCommand().lower()

            if 'wikipedia' in query:
                speak('searching wikipedia...')
                query=query.replace('wikipedia','')
                results=wikipedia.summary(query,sentences=2)
                speak('According to wikipedia')
                print(results)
                speak(results)

            elif 'youtube' in query:
                speak('opening Youtube')
                webbrowser.register('chrome',
	            None,
	            webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
                webbrowser.get('chrome').open('https://youtube.com')

            elif 'git' in query:
                speak('opening Github')
                webbrowser.register('chrome',
	            None,
	            webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
                webbrowser.get('chrome').open('https://github.com')

            elif 'mail' in query:
                speak('opening gmail')
                webbrowser.register('chrome',
	            None,
	            webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
                webbrowser.get('chrome').open('https://gmail.com')

            elif 'google' in query:
                speak('opening google')
                webbrowser.register('chrome',
	            None,
	            webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
                webbrowser.get('chrome').open('https://google.com')

            elif 'the time' in query:
                strTime=datetime.datetime.now().strftime("%H:%M")
                speak(f'sir, the time is {strTime}')
            
            elif 'open code' in query:
                speak("opening vs code")
                path='"C:\\Users\SHUBHAM\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe"'
                os.startfile(path)

            elif 'NoneType' in query:
                speak("please say that again")

            elif 'quit friday' in query:
                speak('good bye')
                break



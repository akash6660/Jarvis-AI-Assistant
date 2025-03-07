import pyttsx3
import speech_recognition as sr
import eel
import time


def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 174)

    if hasattr(eel, 'DisplayMessage'):
        eel.DisplayMessage(text)

    engine.say(text)

    if hasattr(eel, 'senderText'):
        eel.senderText(text)

    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    r.energy_threshold = 300  # Adjust based on noise level

    with sr.Microphone() as source:
        print('Listening...')
        if hasattr(eel, 'DisplayMessage'):
            eel.DisplayMessage('Listening...')

        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=6)
            print('Recognizing...')
            if hasattr(eel, 'DisplayMessage'):
                eel.DisplayMessage('Recognizing...')
            
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            
            if hasattr(eel, 'DisplayMessage'):
                eel.DisplayMessage(query)

            time.sleep(2)
            return query.lower()

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            if hasattr(eel, 'DisplayMessage'):
                eel.DisplayMessage("Sorry, I could not understand.")
            return ""

        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            if hasattr(eel, 'DisplayMessage'):
                eel.DisplayMessage("Speech service error.")
            return ""

        except Exception as e:
            print(f"Error: {e}")
            return ""


@eel.expose
def allCommands(message=1):
    if message == 1:
        query = takecommand()
    else:
        query = message

    if hasattr(eel, 'senderText'):
        eel.senderText(query)

    try:
        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
        elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)
        else:
            from engine.features import chatBot
            chatBot(query)

    except Exception as e:
        print(f"Error executing command: {e}")

    if hasattr(eel, 'ShowHood'):
        eel.ShowHood()


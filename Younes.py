#Assistant welcher mit Sprache aktiviert wird

from __future__ import print_function
import os.path
import os
import time
import gtts
import speech_recognition as sr


def speak(text):
    language = 'en'
    text_gen = gtts(text=text, language=language, slow=False)
    text_gen.save("sample.mp3")
    os.system("mpg321 sample.mp3")
    
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said.lower()


WAKE = "hey tim"
print("Start")

while True:
    print("Listening")
    text = get_audio()

    if text.count(WAKE) > 0:
        speak("I am ready")
        text = get_audio()
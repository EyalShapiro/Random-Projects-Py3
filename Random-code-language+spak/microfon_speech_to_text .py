import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak now!")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("You said: ", text)
except sr.UnknownValueError:
    print("Sorry, I could not understand what you said.")
except sr.RequestError as e:
    print(
        "Could not request results from Google Speech Recognition service; {0}".format(e))

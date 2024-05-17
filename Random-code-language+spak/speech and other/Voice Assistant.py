import pyttsx3
import speech_recognition as sr


def take_commands():
    rec = sr.Recognizer()
    # opening physical microphone of computer
    with sr.Microphone() as source:
        print("Listening")
        rec.pause_threshold = 0.7
        # storing audio/sound to audio variable
        audio = rec.listen(source)
        try:
            print("Recognizing")
            # Recognizing audio using google api
            Query = rec.recognize_google(audio)
            print("the query is printed='", Query, "'")
        except Exception as e:
            print(e)
            print("Say that again sir")
            # returning none if there are errors
            return "None"
    # returning audio as text
    return Query


# creating Speak() function to giving Speaking power
# to our voice assistant


def Speak(audio):
    # initializing pyttsx3 module
    engine = pyttsx3.init()
    # anything we pass inside engine.say(),
    # will be spoken by our voice assistant
    engine.say(audio)
    engine.runAndWait()


# Driver Code
if __name__ == "__main__":
    # using while loop to communicate infinitely
    while True:
        command = take_commands()
        if "exit" in command:
            Speak("Sure sir! as your wish, bai")
            break
        if "insta" in command:
            Speak("Best python page on instagram is pythonhub")
        if "learn" in command:
            Speak("copyassignment website is best to learn python")
        if "code" in command:
            Speak("תלמד ילד")

import pyttsx3

class TEXT_CONVERTER():
    def __init__(self, text: str):
        self.text_speech = pyttsx3.init()
        self.text_speech.say(text)
        self.text_speech.runAndWait()
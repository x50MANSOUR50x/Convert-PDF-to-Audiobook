import pyttsx3
import os

class TEXT_CONVERTER():
    def __init__(self, text: str, pdf_path: str):
        self.text_speech = pyttsx3.init()
        self.text_speech.say(text)
        os.system(pdf_path)
        self.text_speech.runAndWait()
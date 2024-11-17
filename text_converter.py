import pyttsx3
import os
import pyautogui



class TEXT_CONVERTER():
    def __init__(self, text: str, pdf_path: str):
        self.text_speech = pyttsx3.init()
        for page in text:
            # print(page)
            self.text_speech.say(page)
            # print(f"{ { pdf_path } }")
            # print(pdf_path)
            # if ' ' in pdf_path:
            #     pdf_path = pdf_path.replace(' ', '-')
            # print(pdf_path)
            os.startfile(filepath=pdf_path)
            self.text_speech.runAndWait()

            pyautogui.hotkey('alt', 'f4')
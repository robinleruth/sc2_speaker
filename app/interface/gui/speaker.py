import pyttsx3

from app.infrastructure.singleton import Singleton


class Speaker(metaclass=Singleton):
    def __init__(self):
        self.engine = pyttsx3.init()

    def add_to_queue(self, action: str):
        self.engine.say(action)

    def run_and_wait(self):
        self.engine.runAndWait()

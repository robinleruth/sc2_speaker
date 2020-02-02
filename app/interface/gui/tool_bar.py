from tkinter import Frame

from app.infrastructure.singleton import Singleton


class ToolBar(Frame, metaclass=Singleton):
    def __init__(self, parent):
        Frame.__init__(self, parent)

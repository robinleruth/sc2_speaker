from tkinter import Frame

from app.interface.gui.main_component import MainComponent


class MainWindow(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.main_component = MainComponent(self)

        self.main_component.pack()

import time

from tkinter import Frame
from tkinter import Label
from tkinter import Button

from app.domain.service.main_service import MainService
from app.interface.gui.aciton_list_view import ActionListView
from app.interface.gui.action_view import ActionView


class RunView(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.service = MainService()

        self.title = Label(self, text='RUN')
        self.middle_frame = Frame(self)
        self.run_button = Button(self, text='Launch', command=self.launch)

        self.title.pack()
        self.middle_frame.pack()
        self.run_button.pack()

    def launch(self):
        while True:
            lst = self.service.get_action_from_queue()
            for action in lst:
                ActionView(self.middle_frame, action).pack()
            time.sleep(1)

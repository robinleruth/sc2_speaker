import time

from tkinter import Frame
from tkinter import Label
from tkinter import Button
from threading import Thread

from app.domain.service.main_service import MainService
from app.interface.gui.aciton_list_view import ActionListView
from app.interface.gui.action_view import ActionView
from app.interface.gui.status_bar import StatusBar


class RunView(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.is_running = True

        self.title = Label(self, text='RUN')
        self.middle_frame = Frame(self)
        self.run_button = Button(self, text='Launch', command=self.launch)
        self.stop_button = Button(self, text='Stop', command=self.stop)

        self.title.pack()
        self.middle_frame.pack()
        self.run_button.pack()
        self.stop_button.pack()
        self.stop_button.pack_forget()

    def launch(self):
        self.service = MainService()
        self.service.run()
        self.is_running = True
        t = Thread(target=self.poll)
        t.setDaemon(True)
        t.start()
        self.run_button.pack_forget()
        self.stop_button.pack()

    def poll(self):
        StatusBar().set_label('Polling has begun')
        self.temp_frame = Frame(self.middle_frame)
        self.temp_frame.pack()
        while True:
            lst = self.service.get_action_from_queue()
            for action in lst:
                StatusBar().set_label(f'Add {action} to queue')
                view = ActionView(self.temp_frame, action)
                view.forget_delete_button()
                view.pack()
            time.sleep(1)
            if not self.is_running:
                break

    def stop(self):
        StatusBar().set_label('Stop')
        self.is_running = False
        self.run_button.pack()
        self.stop_button.pack_forget()
        self.temp_frame.destroy()

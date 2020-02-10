from tkinter import Frame
from tkinter import Button

from app.domain.service.param.param_service import ParamService
from app.domain.model.param import Param
from app.interface.gui.param_list_view import ParamListView
from app.interface.gui.param_view import ParamView
from app.interface.gui.status_bar import StatusBar


class ManageParamView(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.service = ParamService()
        self.add_button = Button(self, text='Add', command=self.add_param)

        self.frame = Frame(self)
        self.frame.pack()
        self.create_content()
        ParamView(self).pack()

    def add_param(self, name, value):
        try:
            self.service.add_param(name, value)
            self.temp_frame.destroy()
            self.create_content()
        except Exception as e:
            StatusBar().set_label(str(e))

    def create_content(self):
        self.temp_frame = Frame(self.frame)
        self.temp_frame.pack()
        lst = self.service.get_all()
        ParamListView(self.temp_frame, lst, self.service).pack()

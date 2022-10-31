import tkinter as tk
from GUI.menubar import Menubar
from GUI.auth_middleware import Auth
from GUI.create_pass_middleware import CreatePassword
from GUI.table import DataView
from auth.scrambler import encryption
from auth.decoder import decryption
import os
import dotenv
import create_database

dotenv.load_dotenv()


class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configs()

    def configs(self):
        self.title('MyNotes')
        self.geometry('500x550+500+50')
        self.minsize(500, 100)
        self.maxsize(500, 700)
        self.__background_color()
        self.protocol('<WM_DELETE_WINDOW>', exit_on_app)
        self.config(menu=Menubar(self))
        self.__auth()

    def __auth(self):
        password = os.getenv("PASSWORD")
        if password:
            autologin = int(os.getenv('PASSWORD_STATE'))
            if autologin:
                decryption()
                DataView(self)
            else:
                Auth(self)
        else:
            CreatePassword(self)

    def __background_color(self):
        with open('color.txt') as file:
            color = file.readlines()
        choose_col, def_col = color
        try:
            self["background"] = choose_col.strip().split('=')[1]
        except Exception as ex:
            self["background"] = def_col.strip().split('=')[1]

    def refresh_widgets(self):
        all_widgets = [w for w in self.children]
        for widget in all_widgets:
            if widget != '!menubar':
                self.nametowidget(widget).destroy()
        self.__background_color()


def exit_on_app():
    for _, _, files in os.walk("."):
        for filename in files:
            if filename == 'Notes':
                encryption()


if __name__ == '__main__':
    try:
        with open('Notes.crt'):
            pass
    except FileNotFoundError:
        create_database.Database()
    try:
        app = MyApp()
        app.mainloop()
    except Exception as ex:
        print(f'ERROR>>>{ex}')
        exit_on_app()
    else:
        exit_on_app()

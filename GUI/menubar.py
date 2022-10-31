import tkinter as tk
from GUI.table import DataView
from GUI.create_menu import CreateNote
from GUI.delete_menu import DeleteNote
from GUI.edit_menu import ChooseNote
from GUI.autologin_config import Autologin
from tkinter import colorchooser


class Menubar(tk.Menu):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.option_add('*Font', "Arial 12 bold")
        self.menubar_filling()

    def menubar_filling(self):
        self.add_command(label='Add note', command=self.create_note)
        self.add_command(label='Edit note', command=self.edit_note)
        self.add_command(label='Delete note', command=self.delete_note)
        self.add_command(label='Choose background', command=self.choose_color)
        self.add_command(label='Enter password', command=self.autologin)

    def autologin(self):
        Autologin(self.master)

    def create_note(self):
        CreateNote(self.master)

    def edit_note(self):
        ChooseNote(self.master)

    def delete_note(self):
        DeleteNote(self.master)

    def choose_color(self):
        # variable to store hexadecimal code of color
        color_code = colorchooser.askcolor(title="Choose color")
        with open('color.txt', 'w') as file:
            file.write(f'background color ={color_code[1]}\n'
                       f'default color =#c6ffff')
        self.master["background"] = color_code[1]
        DataView(self.master)

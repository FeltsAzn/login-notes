import tkinter as tk
from tkinter import messagebox as mb
from GUI.table import DataView
from auth.decoder import decryption
from auth.scrambler import encryption
from auth.utils import get_password_hash


class CreatePassword:
    """Окно создания пароля для пользователя"""

    def __init__(self, master):
        self.master = master
        self.root = tk.Toplevel(self.master)
        self.root.configure(background=master['background'])
        self.configs()
        self.elements()
        self.root.mainloop()

    def configs(self) -> None:
        self.root.title('Write a password')
        self.root.geometry('350x170+550+200')
        self.root.minsize(310, 170)
        self.root.maxsize(310, 170)
        self.root.grab_set()

    def elements(self) -> None:
        self.static_text()
        self.text_field()
        self.buttons()

    def static_text(self) -> None:
        first_password = tk.Label(self.root, text='Password:', background=self.root["background"])
        second_password = tk.Label(self.root, text='Repeat password:', background=self.root["background"])
        first_password.place(x=65, y=30)
        second_password.place(x=8, y=60)

    def text_field(self) -> None:
        self.first_password_text = tk.Entry(self.root, background='#F8FFDA', width=15, show='*')
        self.second_password_text = tk.Entry(self.root, background='#F8FFDA', width=15, show='*')
        self.first_password_text.place(x=150, y=30)
        self.second_password_text.place(x=150, y=60)

    def check_auto_login_state(self):
        """Загрузка состояния автовхода"""
        self.variable = tk.IntVar()
        with open('.env') as file:
            data = file.readlines()
            state = data[1].split('=')[1]
        self.variable.set(int(state))

    def buttons(self) -> None:
        """Кнопки окна"""
        self.check_auto_login_state()
        button_ok = tk.Button(self.root, text="Create",
                              background="#8DFDC1",
                              foreground="black",
                              padx="3",
                              pady="3",
                              font="12",
                              height=1,
                              width=6,
                              command=self.check_button)
        button_cancel = tk.Button(self.root, text="Cancel",
                                  background="#FD8D8D",
                                  foreground="black",
                                  padx="3",
                                  pady="3",
                                  font="12",
                                  height=1,
                                  width=6,
                                  command=self.root.destroy)

        flag_button = tk.Checkbutton(self.root, text="auto login",
                                     variable=self.variable,
                                     onvalue=1, offvalue=0,
                                     command=self.auto_login,
                                     background=self.root["background"])
        button_ok.place(x=160, y=115)
        button_cancel.place(x=70, y=115)
        flag_button.place(x=150, y=85)

    def check_button(self) -> None:
        """Проверка пароля"""
        first_password: str = self.first_password_text.get()
        second_password: str = self.second_password_text.get()
        if first_password == second_password:
            with open('.env') as file:
                data = file.readlines()
                data[0] = f'PASSWORD={get_password_hash(first_password)}\n'
            with open('.env', 'w') as file:
                file.writelines(data)
            self.root.destroy()
            encryption(first_password)
            decryption(first_password)
            DataView(self.master)
        else:
            mb.showerror('Error', f'Passwords do not match.')

    def auto_login(self):
        """Изменение состояния автовхода"""
        with open('.env') as file:
            data = file.readlines()
            data[1] = f'PASSWORD_STATE={self.variable.get()}\n'
        with open('.env', 'w') as file:
            file.writelines(data)

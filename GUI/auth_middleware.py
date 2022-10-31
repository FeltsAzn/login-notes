import tkinter as tk
from tkinter import messagebox as mb
from auth.decoder import decryption
from GUI.table import DataView


class Auth:
    """Окно проверки пароля пользователя"""

    def __init__(self, master):
        self.master = master
        self.root = tk.Toplevel(self.master)
        self.root.configure(background=master['background'])
        self.configs()
        self.elements()
        self.root.mainloop()

    def configs(self) -> None:
        self.root.title('Write a password')
        self.root.geometry('270x150+550+200')
        self.root.minsize(270, 150)
        self.root.maxsize(270, 150)
        self.root.grab_set()

    def elements(self) -> None:
        self.static_text()
        self.text_field()
        self.buttons()

    def static_text(self) -> None:
        password = tk.Label(self.root, text='Password:', background=self.root["background"])
        password.place(x=10, y=30)

    def text_field(self) -> None:
        self.password_text = tk.Entry(self.root, background='#F8FFDA', width=15, show='*')
        self.password_text.place(x=100, y=30)

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
        button_ok = tk.Button(self.root, text="Add",
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
        button_ok.place(x=140, y=90)
        button_cancel.place(x=50, y=90)
        flag_button.place(x=100, y=60)

    def check_button(self) -> None:
        """Проверка пароля"""
        password: str = self.password_text.get()
        try:
            answer: bool = decryption(password=password)
        except ValueError as ex:
            mb.showerror('Error', f'The database is already open!')
        except FileNotFoundError:
            mb.showerror('Error', f'Missing database!')
        else:
            if answer:
                self.root.destroy()
                DataView(self.master)
            else:
                mb.showerror('Error', f'Access error.\n'
                                      f'Wrong password!')

    def auto_login(self):
        """Изменение состояния автовхода"""
        with open('.env') as file:
            data = file.readlines()
            data[1] = f'PASSWORD_STATE={self.variable.get()}\n'
        with open('.env', 'w') as file:
            file.writelines(data)



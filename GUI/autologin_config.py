import tkinter as tk


class Autologin:
    def __init__(self, master):
        self.master = master
        self.root = tk.Toplevel(self.master)
        self.root.configure(background=master['background'])
        self.configs()
        self.elements()
        self.root.mainloop()

    def configs(self) -> None:
        self.root.title('Auto login')
        self.root.geometry('200x80+550+200')
        self.root.minsize(100, 50)
        self.root.maxsize(310, 170)
        self.root.grab_set()

    def elements(self) -> None:
        self.static_text()
        self.buttons()

    def static_text(self) -> None:
        first_password = tk.Label(self.root, text='Enable automatic login', background=self.root["background"])
        first_password.place(x=10, y=5)

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
        flag_button = tk.Checkbutton(self.root, text="auto login",
                                     variable=self.variable,
                                     onvalue=1, offvalue=0,
                                     command=self.auto_login,
                                     background=self.root["background"])
        flag_button.place(x=30, y=25)

    def auto_login(self):
        """Изменение состояния автовхода"""
        with open('.env') as file:
            data = file.readlines()
            data[1] = f'PASSWORD_STATE={self.variable.get()}\n'
        with open('.env', 'w') as file:
            file.writelines(data)
        self.root.destroy()

import tkinter as tk
from tkinter import messagebox
from GUI.table import DataView
from database.functions import Database


class CreateNote:
    def __init__(self, master):
        self.master = master
        self.root = tk.Toplevel(self.master)
        self.root.configure(background=master['background'])
        self.configs()
        self.elements()
        self.root.mainloop()

    def configs(self) -> None:
        self.root.title('Create new note')
        self.root.geometry('360x200+550+200')
        self.root.minsize(360, 200)
        self.root.maxsize(360, 200)

    def elements(self) -> None:
        self.static_text()
        self.text_field()
        self.buttons()

    def static_text(self) -> None:
        site = tk.Label(self.root, text='Website:', background=self.root["background"])
        login = tk.Label(self.root, text='Login:', background=self.root["background"])
        password = tk.Label(self.root, text='Password:', background=self.root["background"])
        site.place(x=25, y=20)
        login.place(x=40, y=60)
        password.place(x=10, y=100)

    def text_field(self) -> None:
        self.site_text = tk.Entry(self.root, background='#F8FFDA', width=25)
        self.login_text = tk.Entry(self.root, background='#F8FFDA', width=25)
        self.password_text = tk.Entry(self.root, background='#F8FFDA', width=25)
        self.site_text.place(x=100, y=20)
        self.login_text.place(x=100, y=60)
        self.password_text.place(x=100, y=100)

    def buttons(self) -> None:
        button_ok = tk.Button(self.root, text="Add",
                              background="#8DFDC1",
                              foreground="black",
                              padx="3",
                              pady="3",
                              font="12",
                              height=1,
                              width=6,
                              command=self.check_button, )
        button_cancel = tk.Button(self.root, text="Cancel",
                                  background="#FD8D8D",
                                  foreground="black",
                                  padx="3",
                                  pady="3",
                                  font="12",
                                  height=1,
                                  width=6,
                                  command=self.root.destroy)
        button_ok.place(x=220, y=150)
        button_cancel.place(x=80, y=150)

    def check_button(self) -> None:
        site: str = self.site_text.get()
        login: str = self.login_text.get()
        password: str = self.password_text.get()

        if all([site, login, password]):
            try:
                Database().add_data(site, login, password)
            except Exception as ex:
                messagebox.showerror('Error', f'The entered data is incorrect!'
                                              f'\n{ex}')
            else:
                self.root.destroy()
                DataView(self.master)
        else:
            messagebox.showerror('Error', f'Enter data!')

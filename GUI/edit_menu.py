import tkinter as tk
from tkinter import messagebox
from GUI.table import DataView
from database.functions import Database


class ChooseNote:
    def __init__(self, master):
        self.master = master
        self.root = tk.Toplevel(self.master)
        self.root.configure(background=master['background'])
        self.configs()
        self.elements()
        self.root.mainloop()

    def get_notes(self) -> list[tuple]:
        data = Database().get_info()
        return data

    def configs(self) -> None:
        self.root.title('Choose note')
        self.root.geometry('600x260')
        self.root.minsize(350, 200)
        self.root.maxsize(600, 500)
        self.root.grab_set()

    def elements(self) -> None:
        self.static_text()
        self.buttons()

    def static_text(self) -> None:
        self.notes = tk.Listbox(self.root,
                                selectmode=tk.MULTIPLE,
                                font="Arial 12 bold",
                                background='white',
                                justify='left')
        self.notes.place(x=5, y=5, width=450, height=250)
        scrollbar = tk.Scrollbar(self.root, background='#36fc45')
        scrollbar.configure(command=self.notes.yview)
        scrollbar.place(x=438, y=7, height=246)
        self.notes["yscrollcommand"] = scrollbar.set
        self.notes_insert()

    def notes_insert(self) -> None:
        data = self.get_notes()
        for n, website, login, password, _ in data:
            self.notes.insert(tk.END, f'{n}|{website}|{login}|{password}')

    def buttons(self) -> None:
        button_ok = tk.Button(self.root, text="Choose",
                              background="#8DFDC1",
                              foreground="black",
                              padx="3",
                              pady="3",
                              font="12",
                              height=1,
                              width=6,
                              command=self.edit_note)
        button_cancel = tk.Button(self.root, text="Cancel",
                                  background="#FD8D8D",
                                  foreground="black",
                                  padx="3",
                                  pady="3",
                                  font="12",
                                  height=1,
                                  width=6,
                                  command=self.root.destroy)
        button_ok.place(x=480, y=80)
        button_cancel.place(x=480, y=150)

    def edit_note(self) -> None:
        choose_note = list(self.notes.curselection())
        if choose_note and len(choose_note) == 1:
            all_data = self.get_notes()
            info = self.notes.get(choose_note)
            _, website, login, password = info.split('|')
            for num, wb, log, ps, create_date in all_data:
                if website == wb and login == log and password == ps:
                    note_in_db = (num, website, login, password, create_date)
                    self.root.destroy()
                    Editing(self.master, note_in_db)

        else:
            messagebox.showerror('Error', f'Choose only one element!')


class Editing:
    def __init__(self, master, note: tuple):
        self.master = master
        self.root = tk.Toplevel(self.master)
        self.root.configure(background=master['background'])
        self.num, self.website, self.login, self.password, self.create_date = note
        self.configs()
        self.elements()
        self.root.mainloop()

    def configs(self) -> None:
        self.root.title('Edit note')
        self.root.geometry('460x200+550+200')
        self.root.minsize(460, 200)
        self.root.maxsize(460, 200)

    def elements(self) -> None:
        self.static_text()
        self.text_field()
        self.buttons()

    def static_text(self) -> None:
        site = tk.Label(self.root, text='Website:', background=self.root["background"])
        login = tk.Label(self.root, text='Login:', background=self.root["background"])
        password = tk.Label(self.root, text='Password:', background=self.root["background"])
        site.place(x=25, y=27)
        login.place(x=40, y=75)
        password.place(x=10, y=118)

        old_site = tk.Label(self.root, text=f'Old website name: {self.website}', background="#FF6666")
        old_login = tk.Label(self.root, text=f'Old login: {self.login}', background="#FF6666")
        old_password = tk.Label(self.root, text=f'Old password: {self.password}', background="#FF6666")
        old_site.place(x=100, y=2)
        old_login.place(x=100, y=50)
        old_password.place(x=100, y=98)

    def text_field(self) -> None:
        self.site_text = tk.Entry(self.root, background='#F8FFDA', width=35)
        self.login_text = tk.Entry(self.root, background='#F8FFDA', width=35)
        self.password_text = tk.Entry(self.root, background='#F8FFDA', width=35)
        self.site_text.place(x=100, y=27)
        self.login_text.place(x=100, y=75)
        self.password_text.place(x=100, y=123)

    def buttons(self) -> None:
        button_ok = tk.Button(self.root, text="Add",
                              background="#8DFDC1",
                              foreground="black",
                              padx="3",
                              pady="3",
                              font="12",
                              height=1,
                              width=6,
                              command=self.edit_to_database)
        button_cancel = tk.Button(self.root, text="Cancel",
                                  background="#FD8D8D",
                                  foreground="black",
                                  padx="3",
                                  pady="3",
                                  font="12",
                                  height=1,
                                  width=6,
                                  command=self.root.destroy)
        button_ok.place(x=260, y=150)
        button_cancel.place(x=120, y=150)

    def validator(self) -> tuple[str, str, str]:
        site: str = self.site_text.get()
        login: str = self.login_text.get()
        password: str = self.password_text.get()
        if site:
            self.website = site
        if login:
            self.login = login
        if password:
            self.password = password
        return self.website, self.login, self.password

    def edit_to_database(self) -> None:
        new_data = self.validator()
        if any(new_data):
            try:
                site, login, password = new_data
                Database().update_data(self.num, site, login, password, self.create_date)
            except Exception as ex:
                messagebox.showerror('Error', f'The entered data is incorrect!'
                                              f'\n{ex}')
            else:
                self.root.destroy()
                messagebox.showinfo("Operation", "Data has been edited")
                DataView(self.master)

        else:
            messagebox.showerror('Error', f'Enter data!')




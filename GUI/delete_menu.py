import tkinter as tk
from tkinter import messagebox
from GUI.table import DataView
from database.functions import Database


class DeleteNote:
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
        self.root.title('Delete notes')
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
        for num, website, login, password, _ in data:
            self.notes.insert(tk.END, f'{num}|{website}|{login}|{password}')

    def buttons(self) -> None:
        button_ok = tk.Button(self.root, text="Choose",
                              background="#8DFDC1",
                              foreground="black",
                              padx="3",
                              pady="3",
                              font="12",
                              height=1,
                              width=6,
                              command=self.delete_notes, )
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

    def delete_notes(self) -> None:
        choose_notes = list(self.notes.curselection())
        if choose_notes:
            answer = messagebox.askquestion('Warning', "Are you shure to delete this note?")
            if answer == 'yes':
                delete_notes = []
                all_data = [i for i in self.get_notes()]
                for note in choose_notes:
                    info = self.notes.get(note)
                    _, website, login, password = info.split('|')
                    for num, wb, log, ps, create_date in all_data:
                        if website == wb and login == log and password == ps:
                            delete_notes.append((num, create_date))
                try:
                    for n, cr_date in delete_notes.copy():
                        Database().delete_data(num=n, create_date=cr_date)
                except Exception as ex:
                    messagebox.showerror('Error', f'The entered data is incorrect!'
                                                  f'\n{ex}')
                else:
                    self.root.destroy()
                    messagebox.showinfo('Info', 'Data deleted successfully!')
                    DataView(self.master)
        else:
            messagebox.showerror('Error', f'Enter data!')

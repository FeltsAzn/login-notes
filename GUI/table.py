from database.functions import Database
import tkinter as tk


class DataView:
    __instance = None

    def __new__(cls, master, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(DataView, cls).__new__(cls)

        else:
            master.refresh_widgets()

        return cls.__instance

    def __init__(self, master):
        self.info = tk.Text(master, height=30, font="Arial 12 bold", width=50)
        self.info.configure(background=master["background"])
        self.__filling_data()
        self.__scroll_view()
        self.listbox_place()

    def listbox_place(self) -> None:
        self.info.pack(expand=tk.YES, side=tk.LEFT, fill=tk.BOTH)
        self.info.configure(state="disabled")

    def __filling_data(self) -> None:
        all_text = Database().get_info()
        counter = 0
        for num, website, login, password, create_date in all_text:
            if counter == 0:
                text = f' {num}. {website} ||| {create_date}\n' \
                       f' login: {login}\n' \
                       f' password: {password}\n\n' \
                       f'{"#"*50}\n'
                counter += 1
            else:
                text = f'\n {num}. {website} ||| {create_date}\n' \
                       f' login: {login}\n' \
                       f' password: {password}\n\n' \
                       f'{"#"*50}\n'
            self.info.insert("end", text, "bold")

    def __scroll_view(self) -> None:
        """Scroll bar for table"""
        scroll = tk.Scrollbar()
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        scroll.config(command=self.info.yview)
        self.info["yscrollcommand"] = scroll.set

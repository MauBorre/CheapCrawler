import tkinter as tk

from config_writer import write_to_conf

from crawler import run_crawler

"""
    nuevo punto de entrada... deberia abrirse al hacer doble click en el
    system-tray icon (desktop toast notifications...)
"""

class CheapCrawlerInterface(tk.Frame):
    default_amt_tag = "Cantidad"
    default_item_tag = "Ingrese articulo"
    button_tag = "Search!"

    def __init__(self, master=None):
        super().__init__(master)
        self.pack(padx=20, pady=10)
        self.create_components()

    def create_components(self):
        # Amount label
        tk.Label(self, text=self.default_amt_tag).grid(column=0, row=0)
        self.amt_entry = tk.Entry(self, justify="center", fg="blue", width=15)
        self.amt_entry.config(validate="key")
        self.amt_entry.grid(column=0, row=1)

        # Item label
        tk.Label(self, text=self.default_item_tag).grid(column=1, row=0)
        self.item_entry = tk.Entry(self, justify="center", fg="green", width=15)
        self.item_entry.config(validate="key")
        self.item_entry.grid(column=1, row=1)

        # Search btn
        self.search_btn = tk.Button(self, text=self.button_tag, justify="center", command=self.search_command)
        self.search_btn.grid(column=0, row=2, columnspan=2)
    
    def search_command(self):
        # obtener los valores del campo de entrada (validacion?)
        amount = self.amt_entry.get()
        item = self.item_entry.get()
        # escribe el archivo config.txt
        write_to_conf(amount, item)
        # ejecuta crawler.py
        run_crawler(amount, item)
        
        # mensaje de todo ok?

if __name__ == "__main__":
    root = tk.Tk()
    root.title("CheapCrawler")
    app = CheapCrawlerInterface(master=root)
    root.mainloop()
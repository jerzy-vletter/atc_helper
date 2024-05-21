import tkinter as tk


class CreateMainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("atc helper")
        self.attributes('-topmost', True)
        self.frame = tk.Frame(self)
        self.state = False
        self.minsize(300, 400)
        self.eval('tk::PlaceWindow . center')

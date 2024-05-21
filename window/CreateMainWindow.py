import tkinter as tk


class CreateMainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("atc helper")
        self.attributes('-topmost', True)
        self.frame = tk.Frame(self)
        self.frame.pack()
        self.state = False
        self.minsize(400, 400)
        self.eval('tk::PlaceWindow . center')

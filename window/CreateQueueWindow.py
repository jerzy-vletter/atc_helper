import tkinter as tk


class CreateQueueWindow(tk.Toplevel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("aircraft queue")
        self.attributes('-topmost', True)
        self.frame = tk.Frame(self)
        self.state = False
        self.minsize(300, 400)

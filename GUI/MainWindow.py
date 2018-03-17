from tkinter import Label, Button


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Main")

        self.label = Label(self.root,
                           text="TODO: Replace with more useful text")
        self.label.pack()

        self.b_close = Button(self.root,
                              text="Close",
                              command=self.root.quit)
        self.b_close.pack()
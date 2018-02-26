import tkinter as tk

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.width = 700
        self.height = 500
        self.root.title("Main")

        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height)
        self.canvas.configure(background='light blue')
        self.canvas.pack()

        self.label = tk.Label(self.root,
                           text="TODO: Replace with more useful text")
        self.label.configure(background="light blue")
        self.label.place(x=250, y=20)

        self.b_close = tk.Button(self.root,
                              text="Close",
                              command=self.root.quit)
        self.b_close.place(x=10,y=450)

        self.button1 = tk.Button(self.root, text="Button1", width=5, height=3)
        self.button1.configure(background="red")
        self.button1.place(x=10, y=50)

        self.button2 = tk.Button(self.root, text="Button2", width=5, height=3)
        self.button2.configure(background="yellow")
        self.button2.place(x=10, y=110)

        self.button3 = tk.Button(self.root, text="Button3", width=5, height=3)
        self.button3.configure(background="orange")
        self.button3.place(x=10, y=170)

        self.button4 = tk.Button(self.root, text="Button4", width=5, height=3)
        self.button4.configure(background="green")
        self.button4.place(x=10, y=230)

        self.button5 = tk.Button(self.root, text="Button5", width=5, height=3)
        self.button5.configure(background="blue")
        self.button5.place(x=10, y=290)

        self.button6 = tk.Button(self.root, text="Button6", width=5, height=3)
        self.button6.configure(background="purple")
        self.button6.place(x=10, y=350)

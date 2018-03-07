import tkinter as tk
from tkinter.font import Font
from Command import *
from threading import Thread
import time

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.width = 700
        self.height = 500
        self.root.title("Main")
        self.commands = []

        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height)
        self.canvas.configure(background='light blue')
        self.canvas.pack()

        self.label = tk.Label(self.root,
                              text="Robot Controller: Sean White & Kaitlyn Icopini")
        self.label.configure(background="light blue")
        self.label.place(x=200, y=20)

        self.btn_head = tk.Button(self.root, text="Head",
                                  width=5, height=3, command=self.on_head_btn_click)
        self.btn_head.configure(background="purple")
        self.btn_head.place(x=10, y=50)

        self.btn_body = tk.Button(self.root, text="Body",
                                  width=5, height=3, command=self.on_body_btn_click)
        self.btn_body.configure(background="yellow")
        self.btn_body.place(x=10, y=110)

        self.btn_move = tk.Button(self.root, text="Move",
                                  width=5, height=3, command=self.on_move_btn_click)
        self.btn_move.configure(background="orange")
        self.btn_move.place(x=10, y=170)

        self.btn_start = tk.Button(self.root, text="Start",
                                   width=5, command=self.on_start_btn_click)
        self.btn_start.configure(background="green")
        self.btn_start.place(x=10, y=450)

        self.btn_stop = tk.Button(self.root, text="Clear",
                                  width=5, command=self.on_clear_btn_click)
        self.btn_stop.configure(background="red")
        self.btn_stop.place(x=90, y=450)

        self.btn_close = tk.Button(self.root, text="Close",
                                   width=5, command=self.root.quit)
        self.btn_close.place(x=600, y=450)

    def on_body_btn_click(self):
        def save():
            args = []
            pos = 6000

            # Suck it, String.equals()
            if variable == "Left":
                pos = 8000
            elif variable == "Right":
                pos = 4000

            args.append(pos)

            cmd = BodyCommand(args)
            self.commands.append(cmd)

            window.destroy()

        window = tk.Toplevel(self.root)

        variable = tk.StringVar(self.root)
        variable.set("Straight")

        menu = tk.OptionMenu(window, variable, "Left", "Straight", "Right")
        menu.pack()

        btn_save = tk.Button(window, text="Save", command=save)
        btn_save.pack()

    def on_head_btn_click(self):
        def save():
            pos_h = 6000
            pos_v = 6000

            if variable_hor == "Left":
                pos_h = 8000
            elif variable_hor == "Right":
                pos = 4000

            if variable_ver == "Up":
                pos_v = 8000
            elif variable_hor == "Down":
                pos_v = 4000

            cmd_h = HeadCommand([4, pos_h])
            cmd_v = HeadCommand([3, pos_v])

            self.commands.append(cmd_h)
            self.commands.append(cmd_v)

            window.destroy()

        window = tk.Toplevel(self.root)

        variable_hor = tk.StringVar(self.root)
        variable_hor.set("Straight")

        variable_ver = tk.StringVar(self.root)
        variable_ver.set("Straight")

        menu_hor = tk.OptionMenu(window, variable_hor, "Left", "Straight", "Right")
        menu_hor.pack()

        menu_ver = tk.OptionMenu(window, variable_ver, "Up", "Straight", "Down")
        menu_ver.pack()

        btn_save = tk.Button(window, text="Save", command=save)
        btn_save.pack()

    def on_move_btn_click(self):
        def save():
            pin = 1
            direction = 1

            if variable == "Reverse":
                pin = 1
                direction = -1
            elif variable == "Left":
                pin = 2
                direction = 1
            elif variable == "Right":
                pin = 2
                direction = -1

            cmd = MoveCommand([pin, direction, int(box.get())])
            self.commands.append(cmd)

            window.destroy()

        window = tk.Toplevel(self.root)

        variable = tk.StringVar(self.root)
        variable.set("Forward")

        menu = tk.OptionMenu(window, variable, "Forward", "Left", "Right", "Reverse")
        menu.pack()

        box = tk.Spinbox(window,from_=1, to=100, width=3,
               font=Font(family='Helvetica', size=36, weight='bold'))
        box.pack()

        btn_save = tk.Button(window, text="Save", command=save)
        btn_save.pack()

    def on_start_btn_click(self):
        flash_thrd = Thread(target=self.flash())
        flash_thrd.start()

        cmd_thrd = Thread(target=self.run_commands())
        cmd_thrd.start()

        self.commands = []

    def on_clear_btn_click(self):
        self.commands = []

    def flash(self):
        self.btn_start.flash()

    def run_commands(self):
        for command in self.commands:
            command.run_command()

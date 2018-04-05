import tkinter as tk
from tkinter.font import Font
from Command import *
from threading import Thread
import time

class MainWindow:
    def __init__(self, root):
        self.server_thread = ServerThreadIntermediary().get_server_thread(self)
        self.root = root
        self.width = 800
        self.height = 500
        self.boxes = [0]
        self.root.title("Main")
        self.commands = []

        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height)
        self.canvas.configure(background='light cyan')
        self.canvas.pack()

        #Title--------------------------------------------------------------------
        self.title = tk.Label(self.root, font=("Arial", 18),
                              text="Robot Controller")
        self.title.configure(background="light cyan")
        self.title.place(x=320, y=20)

        self.by = tk.Label(self.root, font=("Arial", 10), text="Sean White\nKaitlyn Icopini")
        self.by.configure(background="light cyan")
        self.by.place(x=700, y=10)

        #Head---------------------------------------------------------------------
        self.btn_head = tk.Button(self.root, font=("Arial", 12), text="Head",
                                  width=5, height=3, command=self.on_head_btn_click)
        self.btn_head.configure(background="purple1")
        self.btn_head.place(x=10, y=80)

        #Body---------------------------------------------------------------------
        self.btn_body = tk.Button(self.root, font=("Arial", 12), text="Body",
                                  width=5, height=3, command=self.on_body_btn_click)
        self.btn_body.configure(background="yellow")
        self.btn_body.place(x=10, y=150)

        #Move---------------------------------------------------------------------
        self.btn_move = tk.Button(self.root, font=("Arial", 12), text="Move",
                                  width=5, height=3, command=self.on_move_btn_click)
        self.btn_move.configure(background="orange")
        self.btn_move.place(x=10, y=220)

        #Talk---------------------------------------------------------------------
        self.btn_talk = tk.Button(self.root, font=("Arial", 12), text="Talk",
                                  width=5, height=3, command=self.on_talk_btn_click)
        self.btn_talk.configure(background="deep sky blue")
        self.btn_talk.place(x=10, y=290)

        #Start--------------------------------------------------------------------
        self.btn_start = tk.Button(self.root, font=("Arial", 12), text="Start",
                                   width=5, command=self.on_start_btn_click)
        self.btn_start.configure(background="green")
        self.btn_start.place(x=10, y=450)

        #Stop/Clear---------------------------------------------------------------------
        self.btn_stop = tk.Button(self.root, font=("Arial", 12), text="Clear",
                                  width=5, command=self.clear)
        self.btn_stop.configure(background="red")
        self.btn_stop.place(x=90, y=450)

        #Close--------------------------------------------------------------------
        self.btn_close = tk.Button(self.root, font=("Arial", 12), text="Close",
                                   width=5, command=self.root.quit)
        self.btn_close.place(x=self.width-100, y=450)


    def on_body_btn_click(self):
        def save():
            args = []
            pos = 6000

            # Suck it, String.equals()
            if variable.get() == "Left":
                pos = 8000
            elif variable.get() == "Right":
                pos = 4000

            args.append(pos)

            cmd = BodyCommand(args)
            self.commands.append(cmd)
            self.boxes.append(self.boxes[-1]+90)
            self.canvas.create_rectangle(self.boxes[-1], 130, self.boxes[-1]+80, 331, fill="yellow", width=0)

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

            if variable_hor.get() == "Left":
                pos_h = 8000
            elif variable_hor.get() == "Right":
                pos = 4000

            if variable_ver.get() == "Up":
                pos_v = 8000
            elif variable_ver.get() == "Down":
                pos_v = 4000

            cmd_h = HeadCommand([4, pos_h])
            cmd_v = HeadCommand([3, pos_v])

            self.commands.append(cmd_h)
            self.commands.append(cmd_v)

            self.boxes.append(self.boxes[-1]+90)
            self.canvas.create_rectangle(self.boxes[-1], 130, self.boxes[-1]+80, 331, fill="purple1", width=0)

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

            if variable.get() == "Reverse":
                pin = 1
                direction = -1.85
            elif variable.get() == "Left":
                pin = 2
                direction = 1
            elif variable.get() == "Right":
                pin = 2
                direction = -1.85

            cmd = MoveCommand([pin, direction, int(box.get())])
            self.commands.append(cmd)

            self.boxes.append(self.boxes[-1]+90)
            self.canvas.create_rectangle(self.boxes[-1], 130, self.boxes[-1]+80, 331, fill="orange", width=0)

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

    def on_talk_btn_click(self):
        def save():
            args = []
            args.append(variable.get())
            cmd = TalkCommand(args)
            self.commands.append(cmd)
            self.boxes.append(self.boxes[-1]+90)
            self.canvas.create_rectangle(self.boxes[-1], 130, self.boxes[-1]+80, 331, fill="deep sky blue", width=0)

            window.destroy()

        window = tk.Toplevel(self.root)

        variable = tk.StringVar(self.root)
        variable.set("I won't enjoy this.")

        menu = tk.OptionMenu(window, variable,
                            "I won't enjoy this.",
                            "I think you ought to know, I'm feeling very depressed.",
                            "I have a million ideas. They all point to certain death.,",
                            "I'd give you advice, but you wouldn't listen. No one ever does.",
                            "It gives me a headache just trying to think down to your level.",
                            "This is the sort of thing you lifeforms enjoy, is it?")
        menu.pack()

        btn_save = tk.Button(window, text="Save", command=save)
        btn_save.pack()

    def on_start_btn_click(self):
        cmd_thrd = Thread(target=self.run_commands())
        cmd_thrd.start()

        self.clear()

    def clear(self):
        self.commands = []
        self.boxes = [0]
        self.canvas.create_rectangle(90, 130, 800, 331, fill="light cyan", width=0)

    def run_commands(self):
        for command in self.commands:
            self.btn_start.flash()
            command.run_command()

    def take_voice_command(self, command):
        tokens = command.split(' ')

        if tokens[0] == 'start' or tokens[0] == 'run':
            self.run_commands()
        if tokens[0] == 'clear':
            self.clear()

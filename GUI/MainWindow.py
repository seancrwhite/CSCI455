import threading
import tkinter as tk
#from RobotController import RobotController

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.width = 700
        self.height = 500
        self.root.title("Main")
        self.stop_button_pressed = False
        #self.controller = RobotController()
        self.commands = []

        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height)
        self.canvas.configure(background='light blue')
        self.canvas.pack()

        self.label = tk.Label(self.root,
                              text="Robot Controller: Sean White & Kaitlyn Icopini")
        self.label.configure(background="light blue")
        self.label.place(x=250, y=20)

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

        self.btn_stop = tk.Button(self.root, text="Stop",
                                  width=5, command=self.on_stop_btn_click)
        self.btn_stop.configure(background="red")
        self.btn_stop.place(x=90, y=450)

        self.btn_close = tk.Button(self.root, text="Close",
                                   width=5, command=self.root.quit)
        self.btn_close.place(x=600, y=450)

    def on_body_btn_click(self):
        print("Not Yet Implmented.")

    def on_head_btn_click(self):
        print("Not Yet Implmented.")

    def on_move_btn_click(self):
        print("Not Yet Implmented.")

    def on_start_btn_click(self):
        for command in commands:
            if not stop_button_pressed:
                command.run_command()
            else:
                break

    def on_stop_btn_click(self):
        self.stop_button_pressed = True

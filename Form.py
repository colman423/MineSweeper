# coding=utf-8
from tkinter import *
from tkinter import messagebox
from PIL.ImageTk import PhotoImage
from MineBlock import MineBlock
import MineImages as IMG
import MineStatus as STATUS
import sys
from TimeCounter import TimeCounter


class Form(Tk):
    mine_images = [0]*10
    row = 0
    col = 0
    mine_buttons = None
    safe_block = -1
    timeCounter = None

    def __init__(self, row, col, bomb, data):
        super().__init__()
        self.row, self.col = row, col
        self.init_menubar()
        self.init_button()
        self.init_config()
        self.safe_block = row*col-bomb
        self.set_mines(data)
        self.timeCounter = TimeCounter()
        self.timeCounter.start()

    def init_menubar(self):
        menubar = Menu(self)
        menubar.add_command(label="Hello!")
        menubar.add_command(label="Quit!")

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open")
        filemenu.add_command(label="Save")
        filemenu.add_separator()
        filemenu.add_command(label="Exit")
        menubar.add_cascade(label="File", menu=filemenu)

        # display the menu
        self.config(menu=menubar)

    def init_button(self):
        self.mine_buttons = [[None]*self.col for x in range(self.row)]

        for x in range(self.row):
            for y in range(self.col):
                b = MineBlock(self, row=x, col=y, width=50, height=50)
                b.grid(row=x, column=y, sticky="NEWS")
                b.grid_propagate(0)
                self.mine_buttons[x][y] = b

    def init_config(self):
        self.title("Mine Sweeper")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def set_mines(self, mine_list):
        for x in range(self.row):
            for y in range(self.col):
                item = mine_list[x][y]

                neighbor = item['bombNeighbors']
                img = PhotoImage(IMG.BOMB) if item['isBomb'] else PhotoImage(IMG.LIST[neighbor])

                self.mine_buttons[x][y].set_mine(item['isBomb'], neighbor, img)

    def open_block(self, x, y):
        mine = self.mine_buttons[x][y]
        self.safe_block -= 1

        if self.safe_block==0:
            self.game_success()

        elif mine.neighbor==0:
            print("open neighbor")
            neighbor_list = []
            for i in [ num for num in [-1, 0, 1] if -1 < x+num < self.row]:
                for j in [ num for num in [-1, 0, 1] if -1 < y+num < self.col]:
                    neighbor_list.append(self.mine_buttons[x+i][y+j])

            for item in neighbor_list:
                if item.status==STATUS.HIDE:
                    item.open_block()

    def game_success(self):
        print("game success!")
        self.timeCounter.isAlive = False
        messagebox.showinfo(message="Success!\nYour record is {0:.2f} sec.".format(self.timeCounter.time))
        self.destroy()

    def game_over(self):
        print("game over!")
        messagebox.showwarning(message="Game Over!")
        self.destroy()

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.timeCounter.isAlive = False
            sys.exit()
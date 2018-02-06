# coding=utf-8
from tkinter import *
from PIL.ImageTk import PhotoImage
from mineBlock import MineBlock
import mine_images as IMG


class Form(Tk):
    mine_images = [0]*10
    row = 0
    col = 0
    mine_buttons = None

    def __init__(self, row, col):
        super().__init__()
        self.row, self.col = row, col
        self.init_menubar()
        self.init_button()
        self.init_config()

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

    def set_mines(self, mine_list):
        for x in range(self.row):
            for y in range(self.col):
                item = mine_list[x][y]

                neighbor = item['bombNeighbors']
                img = PhotoImage(IMG.BOMB) if item['isBomb'] else PhotoImage(IMG.LIST[neighbor])

                self.mine_buttons[x][y].set_mine(item['isBomb'], neighbor, img)
        print("end")

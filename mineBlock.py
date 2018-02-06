# coding=utf-8
from tkinter import *
from PIL.ImageTk import PhotoImage
import mine_images as IMG


class MineBlock(Button):
    def __init__(self, master=None, **kw):
        self.row = kw.pop('row', -1)
        self.col = kw.pop('col', -1)
        self.mine = kw.pop('mine', False)
        self.mine_image = PhotoImage(IMG.FLAG)
        self.empty_image = PhotoImage(IMG.EMPTY)
        Button.__init__(self, master, relief=RAISED, image=self.empty_image, **kw)

        self.config(command=self.on_click)

    def on_click(self):
        print("row: {0}, col: {1}".format(self.row, self.col))
        self.config(image=self.mine_image, command='', relief=SUNKEN)

    def set_mine(self, mine, mine_image):
        # pass
        self.mine = mine
        self.mine_image = mine_image

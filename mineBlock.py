# coding=utf-8
from tkinter import *
from threading import Timer
from PIL.ImageTk import PhotoImage
import mine_images as IMG


class MineBlock(Button):
    mouseEntering = False
    def __init__(self, master=None, **kw):
        self.x = kw.pop('row', -1)
        self.y = kw.pop('col', -1)
        self.empty_image = PhotoImage(IMG.EMPTY)

        Button.__init__(self, master, relief=RAISED, image=self.empty_image, **kw)
        # self.bind("<ButtonRelease-1>", self.on_click)
        self.bind("<ButtonRelease-1>", self.on_left_release)
        self.bind("<ButtonRelease-3>", self.on_right_release)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    # def on_click(self, event=None):
    #     print("'x': {0}, 'y': {1}, 'isBomb': {2}, 'neighbor': {3}".format(self.x, self.y, self.isBomb, self.neighbor))
    #     # self.config(image=self.image, command='', relief=SUNKEN)
    #     self.unbind("<ButtonRelease-1>")
    #     Timer(0, lambda:self.config(image=self.image, command='', relief=SUNKEN)).start()

    def on_enter(self, event):
        self.mouseEntering = True

    def on_leave(self, event):
        self.mouseEntering = False

    def on_left_release(self, event):
        if self.mouseEntering:
            print(
                "'x': {0}, 'y': {1}, 'isBomb': {2}, 'neighbor': {3}".
                    format(self.x, self.y, self.isBomb, self.neighbor))
            self.unbind("<ButtonRelease-1>")
            self.unbind("<ButtonRelease-3>")
            self.unbind("<Enter>")
            self.unbind("<Leave>")
            Timer(0, lambda: self.config(image=self.image, command='', relief=SUNKEN)).start()

    def on_right_release(self, event):
        if self.mouseEntering:
            print(
                "'x': {0}, 'y': {1}, 'isBomb': {2}, 'neighbor': {3}".
                    format(self.x, self.y, self.isBomb, self.neighbor))
            self.unbind("<ButtonRelease-1>")
            self.unbind("<ButtonRelease-3>")
            self.unbind("<Enter>")
            self.unbind("<Leave>")
            Timer(0, lambda: self.config(image=self.image, command='', relief=SUNKEN)).start()

    def set_mine(self, isBomb, neighbor, image):
        self.isBomb = isBomb
        self.neighbor = neighbor
        self.image = image

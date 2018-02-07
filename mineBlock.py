# coding=utf-8
from tkinter import *
from PIL.ImageTk import PhotoImage
from threading import Timer
import mine_images as IMG
import mine_status as STATUS


class MineBlock(Button):
    mouseEntering = False

    def __init__(self, master=None, **kw):
        self.x = kw.pop('row', -1)
        self.y = kw.pop('col', -1)

        self.empty_image = PhotoImage(IMG.EMPTY)
        self.flag_image = PhotoImage(IMG.FLAG)
        self.ques_image = PhotoImage(IMG.QUES)
        self.mine_image = self.empty_image

        self.status = STATUS.HIDE
        self.isBomb = False
        self.neighbor = -1

        Button.__init__(self, master, relief=RAISED, image=self.empty_image, **kw)
        self.bind_event()


    def set_mine(self, isBomb, neighbor, image):
        self.isBomb = isBomb
        self.neighbor = neighbor
        self.mine_image = image

    def open_block(self):
        self.unbind_event()
        Timer(0, lambda: self.config(image=self.mine_image, command='', relief=SUNKEN)).start()
        self.status = STATUS.OPEN
        print("'x': {0}, 'y': {1}, 'isBomb': {2}, 'neighbor': {3}".format(self.x, self.y, self.isBomb, self.neighbor))
        if self.isBomb:
            self.master.game_over()
        else:
            self.master.open_neighbor(self.x, self.y)

    def flag_block(self):
        self.status = STATUS.FLAG
        self.config(image=self.flag_image)

    def ques_block(self):
        self.unbind_event(question=True)
        self.status = STATUS.QUES
        self.config(image=self.ques_image)
        pass

    def hide_block(self):
        self.status = STATUS.HIDE
        self.config(image=self.empty_image)
        pass

    def bind_event(self):
        self.bind("<ButtonRelease-1>", self.on_left_release)
        self.bind("<ButtonRelease-3>", self.on_right_release)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def unbind_event(self, question=False):
        if question:
            self.unbind("<ButtonRelease-1>")
        else:
            self.unbind("<ButtonRelease-1>")
            self.unbind("<ButtonRelease-3>")
            self.unbind("<Enter>")
            self.unbind("<Leave>")

    def on_enter(self, event):
        self.mouseEntering = True

    def on_leave(self, event):
        self.mouseEntering = False

    def on_left_release(self, event):
        if self.mouseEntering:
            self.open_block()
            print("open end!")

    def on_right_release(self, event):
        if self.mouseEntering:
            if self.status==STATUS.HIDE:
                self.flag_block()
            elif self.status==STATUS.FLAG:
                self.ques_block()
            else:
                self.bind_event()
                self.hide_block()

# coding=utf-8
from form import Form
from createMine import *


def newGame(row, col, bomb):
    form = Form(row, col)
    data = create_mine(row, col, bomb)
    form.set_mines(data)
    return form

if __name__=="__main__" :
    while True:
        newGame(10, 20, 1).mainloop()

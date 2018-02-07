# coding=utf-8
from Form import Form
from createMine import *


def newGame(row, col, bomb):
    data = create_mine(row, col, bomb)
    form = Form(row, col, bomb, data)
    return form

if __name__=="__main__" :
    while True:
        newGame(10, 20, 1).mainloop()

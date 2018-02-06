# coding=utf-8
from form import Form
from createMine import *


def newGame(row, col, bomb):
    form = Form(row, col)
    data = create_mine(row, col, bomb)
    form.set_mines(data)
    form.mainloop()

if __name__=="__main__" :
    global form
    newGame(5, 10, 10)

# coding=utf-8
from form import Form
from createMine import *

if __name__=="__main__" :
    form = Form(5 ,10)

    data = create_mine(5, 10, 10)
    form.set_mines(data)
    form.mainloop()

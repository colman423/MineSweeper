# coding=utf-8
from PIL import Image

EMPTY = Image.new('RGBA', (1, 1), (0, 0, 0, 0))

FLAG = Image.open("res/flag.png").resize((50, 50))

BOMB = Image.open("res/mine.png").resize((50, 50))

LIST = [Image.open("res/{0}.png".format(i)).resize((50, 50)) for i in range(9)]
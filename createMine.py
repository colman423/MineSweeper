# coding=utf-8
import numpy as np
import scipy.signal


def create_mine(row, col, count):
    mines = np.array([1]*count+[0]*(row*col-count))
    np.random.shuffle(mines)
    mines = mines.reshape((row, col))
    # print(mines)

    neighbors = scipy.signal.convolve2d(mines, np.full((3, 3), 1), mode='same')
    neighbors -= mines
    # print(neighbors)

    # print(np.array(mines, neighbors))
    data = [[{'isBomb':mines[x][y]==1, 'bombNeighbors':neighbors[x][y]} for y in range(col)] for x in range(row)]
    data = np.array(data)
    print(data)

    return data
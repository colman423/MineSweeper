# coding=utf-8
from threading import Thread
from time import sleep

class TimeCounter(Thread):
    def __init__(self):
        super().__init__()
        self.time = 0

    def run(self):
        while self.isAlive:
            print("time++")
            self.time += 0.1
            sleep(0.1)

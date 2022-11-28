#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cgitb import reset
from Commands.PythonCommandBase import ImageProcPythonCommand
from Commands.Keys import Button, Hat, Direction, Stick
import os

class SV_Money(ImageProcPythonCommand):

    NAME = 'SV競り'

    def __init__(self, cam):
        super().__init__(cam)
        self.buy_available = False

    def do(self):
        while True:
            self.buy_available = False
            buy_item = os.listdir("./Template/SV/Auction/Item")
            for i in range(20):
                if self.isContainTemplate("SV/Auction/play.png", 0.9, show_value=True):
                    self.buy_available = True
                    break
                self.wait(1)
            if self.buy_available:
                for i in buy_item:
                    if self.isContainTemplate(f"SV/Auction/Item/{i}", 0.8, show_value=True):
                        
                        self.press(Button.A,0.1,0.5)
                        while not self.isContainTemplate("SV/Auction/bye.png", 0.8):
                            self.press(Button.A,0.1,0.8)
                        self.press(Button.A,0.1,0.5)
                        self.report()
                        self.time()
                        break
                    if i == buy_item[-1]:
                        self.resetGame()
            else:
                self.report()
                self.time()



    def quitGame(self):
        self.press(Button.HOME, 0.1, 0.5)#HOME
        self.press(Button.X,0.05,0.5)
        self.press(Button.A,0.05,0.5)
        while not self.isContainTemplate("SV/Auction/start.png", 0.8):
            self.wait(0.5)
        self.wait(1)
    
    def launchGame(self):
        self.press(Button.A,0.05,1)
        self.press(Button.A,0.05,1)
        while not self.isContainTemplate("SV/Auction/title.png", 0.8, show_value=True):
            self.wait(1)
            self.press(Button.A, 0.5,1)
        self.wait(0.5)
        self.press(Button.A, 0.5,1)
    
    def resetGame(self):
        self.quitGame()
        self.launchGame()

    def report(self):
        while not self.isContainTemplate("SV/Auction/menu.png", 0.8):
            self.press(Button.X,0.1,1)
        self.press(Button.R, 0.1,1)
        self.press(Button.A, 0.1,1)
        while not self.isContainTemplate("SV/Auction/report.png", 0.8, show_value=True):
            self.wait(0.1)
            pass
        self.press(Button.A, 0.1,1)

    def incrementDate(self):
        self.press(Button.A, 0.05, 0.5)
        self.press(Direction.RIGHT)
        self.press(Direction.RIGHT)
        self.press(Direction.UP)
        self.press(Direction.RIGHT)
        self.press(Direction.RIGHT)
        self.press(Direction.RIGHT)
        self.press(Button.A, 0.05, 0.5)
    
    def time(self):
        self.press(Button.HOME, 0.1, 0.5)
        self.press(Direction.DOWN)
        self.press(Direction.RIGHT, 0.55)
        self.press(Button.A, 0.05, 1)
        self.press(Direction.DOWN, 1.2, 0.1)
        self.press(Button.A, 0.05, 0.1)
        self.press(Direction.DOWN, 0.7, 0.1)
        self.press(Button.A)
        self.press(Direction.DOWN, 0.35, 0.1)
        self.incrementDate()
        if self.isContainTemplate("SV/Auction/first.png", 0.8, show_value=True):
            self.press(Button.HOME, 0.05, 1)
            self.press(Button.HOME, 0.05, 1)
            self.report()
            self.time()

        self.quitGame()
        self.launchGame()


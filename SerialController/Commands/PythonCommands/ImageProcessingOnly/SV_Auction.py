#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cgitb import reset
from Commands.PythonCommandBase import ImageProcPythonCommand
from Commands.Keys import Button, Hat, Direction, Stick
import os
import datetime

class SV_Money(ImageProcPythonCommand):

    NAME = 'SV競り'

    def __init__(self, cam):
        super().__init__(cam)

    def do(self):
        while True:
            buy_item = os.listdir("./Template/SV/Auction/Item")
            if self.isContainTemplate("SV/Auction/title_A.png", 0.8):
                self.wait(0.5)
                self.press(Button.A,0.1,0.5)
            
            self.wait(1)

            for i in range(60):
                if self.isContainTemplate("SV/Auction/play.png", 0.8, show_value=True):
                    break
                else:
                    self.wait(1)
            
            for i in buy_item:
                if self.isContainTemplate(f"SV/Auction/Item/{i}", 0.8, show_value=True):
                    
                    self.press(Button.A,0.1,0.5)
                    while not self.isContainTemplate("SV/Auction/bye.png", 0.8):
                        self.press(Button.A,0.1,1)
                    self.press(Button.A,0.1,0.5)
                    self.report()
                    self.time()
                    continue
                if i == buy_item[-1]:
                    self.reset()



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
    
    def reset(self):
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

    def time(self):
        self.quitGame()
        self.press(Direction.DOWN)
        self.press(Direction.RIGHT, 0.55)
        self.press(Button.A, 0.05, 1)
        self.press(Direction.DOWN, 1.2, 0.1)
        self.press(Button.A, 0.05, 0.1)
        self.press(Direction.DOWN, 0.7, 0.1)
        self.press(Button.A)
        self.press(Direction.DOWN, 0.35, 0.1)
        self.press(Button.A, 0.05, 0.5)
        self.press(Direction.RIGHT)
        self.press(Direction.RIGHT)
        self.press(Direction.UP)
        self.press(Direction.RIGHT)
        self.press(Direction.RIGHT)
        self.press(Direction.RIGHT)
        self.press(Button.A, 0.05, 0.5)
        self.press(Button.HOME, 0.1, 1)
        self.launchGame()


import board
import numpy as np

class Player:
    def __init__(self, token):
        self.__token = token
        self.__turn = False
        self.__checkedBoxes = []


    def getToken(self):
        return self.__token

    def changeTurn(self):
        self.__turn = not self.__turn

    def getTurn(self):
        return self.__turn

    def addCheckedBox(self, box):
        self.__checkedBoxes = np.append(self.__checkedBoxes, box.getPosition())

    def getCheckedBoxes(self):
        return self.__checkedBoxes
    

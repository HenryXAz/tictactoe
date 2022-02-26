import numpy as np
import box 

class Board:
    def __init__(self):
        self.__board = np.array([
                                [box.Box(0,0),box.Box(0,1),box.Box(0,2)],
                                [box.Box(1,0),box.Box(1,1),box.Box(1,2)],
                                [box.Box(2,0),box.Box(2,1),box.Box(2,2)]
                                ])

    def printBoard(self):
        print(self.__board[0,0].getToken(), self.__board[0,1].getToken(), self.__board[0,2].getToken())
        print(self.__board[1,0].getToken(), self.__board[1,1].getToken(), self.__board[1,2].getToken())
        print(self.__board[2,0].getToken(), self.__board[2,1].getToken(), self.__board[2,2].getToken())

    def getBox(self, x,y):
        return self.__board[x,y]

    def tickBox(self,x,y, token):
        self.__board[x,y].tick(token)

    def getEmptyBoxes(self):
        availableBoxes = []
        for i in range(3):
            for j in range(3):
                token = self.__board[i,j].getToken()

                if(token == '|___|'):
                    availableBoxes = np.append(availableBoxes, self.__board[i,j].getPosition())

        return availableBoxes
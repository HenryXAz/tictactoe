import numpy as np
import copy
import random
import board
import player
class TicTacToe:
    def __init__(self):
        self.__board = board.Board()
        self.__tokens = ['X', 'O']
        self.__playerOne = player.Player(self.__tokens[0])
        self.__playerOne.changeTurn()
        self.__playerTwo = player.Player(self.__tokens[1])

    def __getCoordenates(self,position):
        x = y = 0

        if(position <=2):
            y = position
        elif(position <=5):
            x = 1
            y = position - 3
        elif(position <=8):
            x = 2
            y = position - 6

        return np.array([x,y])

    def __isInputValid(self, x,y):

        emptyBoxes = self.__board.getEmptyBoxes()

        availableBox = self.__board.getBox(x, y).getPosition()

        if(availableBox in emptyBoxes and y >= 0):
            return True


    def __playerOneTurn(self):
        
        box = 0

        while(True):
            try:
                box = int(input("\nIngrese No. de casilla a marcar "))
                box-=1

                x = self.__getCoordenates(box)[0]
                y = self.__getCoordenates(box)[1]


                if(self.__isInputValid(x,y)):
                    self.__board.tickBox(x,y,self.__playerOne.getToken())
                    checkedBox = self.__board.getBox(x,y)
                    self.__playerOne.addCheckedBox(checkedBox)
                    break
                else:
                    print("Casilla marcada o invalida. Ingrese otra opcion")
                
            except ValueError:
                print("\nValor invalido . Ingrese otra opcion\n")

    def __playerTwoTurn(self):
        
        move = self.__isPossibleWinner(self.__playerOne)
        box = 0

        moveWin = self.__isPossibleWinner(self.__playerTwo)

        if(len(move) != 0):
            for i in range(len(move)):
                if(move[i] in self.__board.getEmptyBoxes()):
                    box = int(move[i])
                else:
                    box = int(random.choice(self.__board.getEmptyBoxes()))
        else:
            if(len(moveWin) !=0):
                for i in range(len(moveWin)):
                    if(moveWin[i] in self.__board.getEmptyBoxes()):
                        box = int(moveWin[i])
                    else:
                        box = int(random.choice(self.__board.getEmptyBoxes()))
            else:
                box = int(random.choice(self.__board.getEmptyBoxes()))
    
        x = self.__getCoordenates(box)[0]
        y = self.__getCoordenates(box)[1]
        

        self.__board.tickBox(x,y,self.__playerTwo.getToken())
        checkedBox = self.__board.getBox(x,y)
        self.__playerTwo.addCheckedBox(checkedBox)

    def __isPossibleWinner(self, player):
        moves = []

        playerLine = player.getCheckedBoxes()
        playerLine.sort()

        if(0 in playerLine and 1 in playerLine):
            moves = np.append(moves, 2)
        if(0 in playerLine and 2 in playerLine):
            moves = np.append(moves, 1)
        if(1 in playerLine and 2 in playerLine):
            moves = np.append(moves,0)

        if(3 in playerLine and 4 in playerLine):
            moves = np.append(moves,5)
        if(3 in playerLine and 5 in playerLine):
            moves = np.append(moves,4)
        if(4 in playerLine and 5 in playerLine):
            moves = np.append(moves,3)

        if(0 in playerLine and 3 in playerLine):
            moves = np.append(moves,6)
        if(0 in playerLine and 6 in playerLine):
            moves = np.append(moves,3)
        if(3 in playerLine and 6 in playerLine):
            moves = np.append(moves,0)

        if(1 in playerLine and 4 in playerLine):
            moves = np.append(moves,7)
        if(1 in playerLine and 7 in playerLine):
            moves = np.append(moves,4)
        if(4 in playerLine and 7 in playerLine):
            moves = np.append(moves,1)

        if(2 in playerLine and 5 in playerLine):
            moves = np.append(moves,8)
        if(2 in playerLine and 8 in playerLine):
            moves = np.append(moves,5)
        if(5 in playerLine and 8 in playerLine):
            moves = np.append(moves,2)

        if(0 in playerLine and 4 in playerLine):
            moves = np.append(moves,8)
        if(0 in playerLine and 8 in playerLine):
            moves = np.append(moves, 4)
        if(4 in playerLine and 8 in playerLine):
            moves = np.append(moves,0)

        if(2 in playerLine and 4 in playerLine):
            moves = np.append(moves,6)
        if(2 in playerLine and 6 in playerLine):
            moves = np.append(moves,4)
        if(4 in playerLine and 6 in playerLine):
            moves = np.append(moves,2)

        return moves

    def __winner(self,player):
        isWinner = False

        playerLine = player.getCheckedBoxes()
        playerLine.sort()

        if(0 in playerLine and 1 in playerLine and 2 in playerLine):
            isWinner = isWinner or True
        if(3 in playerLine and 4 in playerLine and 5 in playerLine):
            isWinner = isWinner or True
        if(6 in playerLine and 7 in playerLine and 8 in playerLine):
            isWinner = isWinner or True
        if(0 in playerLine and 3 in playerLine and 6 in playerLine):
            isWinner = isWinner or True
        if(1 in playerLine and 4 in playerLine and 7 in playerLine):
            isWinner = isWinner or True
        if(2 in playerLine and 5 in playerLine and 8 in playerLine):
            isWinner = isWinner or True
        if(0 in playerLine and 4 in playerLine and 8 in playerLine):
            isWinner = isWinner or True
        if(2 in playerLine and 4 in playerLine and 6 in playerLine):
            isWinner = isWinner or True
        
        return isWinner


    def play(self):
        end = 0

        print('\n--------------------Jugo del TicTacToe------------------------------\n')

        self.__board.printBoard()

        while(True):

            if(len(self.__board.getEmptyBoxes()) == 0):
                self.__board.printBoard()
                print("Juego Empatado")
                break

            if(self.__playerOne.getTurn()):
                self.__playerOneTurn()
                if(self.__winner(self.__playerOne)):
                    self.__board.printBoard()
                    print("\n\nJugador 1 gano el juego\n\n\n")
                    break
            elif(self.__playerTwo.getTurn()):
                self.__playerTwoTurn()
                if(self.__winner(self.__playerTwo)):
                    self.__board.printBoard()
                    print('\nLa maquina gano\n')
                    break


            self.__playerOne.changeTurn()
            self.__playerTwo.changeTurn()
            self.__board.printBoard()
            print('\n\n')

            while(True):
                try:
                    end = int(input("Desea continuar con el juego? 1.Si 2.No "))

                    break
                except ValueError:
                    print('\nIngrese una opcion valida\n')

            if(end == 2):
                break

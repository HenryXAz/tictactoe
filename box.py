class Box:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        self.__position = (3*x) + y
        self.__token = '|___|'

    def getCoordenates(self):
        return [self.__x, self.__y]

    def getPosition(self):
        return self.__position

    def tick(self,token):
        self.__token = '|_' + token  +'_|' 

    def getToken(self):
        return self.__token
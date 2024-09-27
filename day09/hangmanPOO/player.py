import os;

class Player :
    penalties : int;
    playerWord : str;

    def __init__(self, pWord : str) :
        self.penalties = 0;
        self.playerWord = pWord;

    def getPlayerWord(self) :
        return self.playerWord;
    
    def setPenalties(self, p : int) :
        self.penalties = p;

    def getPenalties(self) :
        return self.penalties;
from PartOfGame import Participient_Of_Game
from CheckInput import AskForInput
from GameUtilites import WriteLog
from GlobalVarNames import *   # файл с глобальными переменными в игре


# #------------------------------------------------------------------------------------------------
class Player(Participient_Of_Game):     #класс игрока
    def __init__(self, name, bet=0,score=0):
        super().__init__(name, score)
        self.bet=bet              #Обнуление ставки игрока перед началом новой игры

    def RequireForPlayerBet(self):
        print('')
        print('***Start blackjack game***')
        WriteLog(LogFileName, '***Start blackjack game***',False)
        self.bet=AskForInput('PLAYER’S BET: ')

    def ShowBet(self):
        TextToShow=f'___player’s bet: {self.bet} chips'
        print(TextToShow)
        WriteLog(LogFileName, TextToShow)

    def Move(self, name_deck):
        RightChoice=False
        while RightChoice==False:
            Input_Move=input("PLAYER'S MOVE: ")
            if Input_Move.lower().strip() in ('hit','stand','double down'):
                RightChoice = True
            else:
                print("Выбор не распознан. Необходимо выбрать среди значений 'hit','stand','double down'")

        WriteLog(LogFileName, "PLAYER'S MOVE: "+Input_Move,False)
        if Input_Move == 'hit':
            super().Hit(name_deck)
        elif Input_Move == 'stand':
            super().Stand()
        elif Input_Move == 'double down':
            super().DoubleDown(name_deck)

from PartOfGame import Participient_Of_Game
from GameUtilites import WriteLog
from GlobalVarNames import *   # файл с глобальными переменными в игре
#------------------------------------------------------------------------------------------------
class Dealer(Participient_Of_Game):     #класс Дилера
    def __init__(self, name, score=0):
        super().__init__(name, score)
        #self.name=name

    def Move(self, name_deck):                 #обработчик хода дилера
        if self.score<17:
            self.Hit(name_deck)
            Choice_of_Dealer='hit'
        else:
            self.Stand()
            Choice_of_Dealer='stand'

        PrintToText="DEALER'S MOVE: "+Choice_of_Dealer
        print(PrintToText)
        WriteLog(LogFileName, PrintToText, False)
from Deck import *
from GameUtilites import WriteLog
from GlobalVarNames import *   # файл с глобальными переменными в игре


#------------------------------------------------------------------------------------------------
class Participient_Of_Game():   #родительский класс для участников (игро, дилер)
    def __init__(self, name, cards=[],IsStand=False,score=0):
        self.name = name
        self.cards=cards
        self.IsStand = IsStand      #индикатор ситуации, когда участник выбрал "stand" в качестве очередного хода
        self.score=score

    def StartCards(self):
        self.hand=[]

    def ShowScore(self):
        add_res=''

        if self.score==21:
            add_res =' (blackjack)'
        elif self.score>21:
            add_res = ' (bust)'
        print(f'___{self.name}: {self.score} {add_res}')
        WriteLog(LogFileName, f'___{self.name}: {self.score} {add_res}')

    def Hit(self, name_deck):              #сдаем карту игроку или дилеру
        card=next(name_deck.HandOverCard())

        self.hand.append(f'{card[0]}-{card[1]}')

        if isinstance(card[0],int):   #прибавляем число очков в зависимости от выбранной карты
            self.score+=int(card[0])
        elif card[0] in ('J','Q','K'):
            self.score += 10
        elif card[0]=='A':      #если выпал туз
            if self.score<11:
                self.score += 11
            else:
                self.score += 1
        if self.score>=21:      #При достижении 21 очка или более игра для игрока или дилера останавливается
            self.IsStand=True

    def Stand(self):
        self.IsStand=True

    def DoubleDown(self, name_deck):
        self.Hit(name_deck)
        self.bet *= 2

    def ShowCards(self):
        TextToShow=f"___{self.name}'s start hand {self.hand}"
        print(TextToShow)
        WriteLog(LogFileName, TextToShow)
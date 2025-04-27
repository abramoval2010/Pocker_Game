import random

All_Сards = [
    (2, 'clubs'), (3, 'clubs'), (4, 'clubs'), (5, 'clubs'), (6, 'clubs'), (7, 'clubs'), (8, 'clubs'), (9, 'clubs'), (10, 'clubs'), ('J', 'clubs'), ('Q', 'clubs'), ('K', 'clubs'),('A', 'clubs'),
    (2, 'diamonds'), (3,'diamonds'), (4,'diamonds'), (5, 'diamonds'), (6, 'diamonds'), (7, 'diamonds'), (8, 'diamonds'), (9, 'diamonds'), (10, 'diamonds'), ('J', 'diamonds'), ('Q', 'diamonds'), ('K', 'diamonds'),('A', 'diamonds'),
    (2, 'hearts'), (3,'hearts'), (4,'hearts'), (5, 'hearts'), (6, 'hearts'), (7, 'hearts'), (8, 'hearts'), (9, 'hearts'), (10, 'hearts'), ('J', 'hearts'), ('Q', 'hearts'), ('K', 'hearts'),('A', 'hearts'),
    (2, 'spades'), (3,'spades'), (4,'spades'), (5, 'spades'), (6, 'spades'), (7, 'spades'), (8, 'spades'), (9, 'spades'), (10, 'spades'), ('J', 'spades'), ('Q', 'spades'), ('K', 'spades'),('A', 'spades'),
]


class Deck():           #класс игральной колоды
    def __init__(self,DeckToPlay=[]):
        self.DeckToPlay=DeckToPlay


    def ShuffleDeck(self):        #функция перетасовка игральной колоды
        Copy_Of_All_Cards=All_Сards.copy()

        global CurrentCardInDeckNum
        CurrentCardInDeckNum = 0
        self.DeckToPlay=[]      #Обнуляем колоду

        for i in range(52):
            num=random.randint(0, 52 - i-1)    #выбираем случайный номер в случайной последовательности
            self.DeckToPlay.append(Copy_Of_All_Cards[num])
            Copy_Of_All_Cards.remove(Copy_Of_All_Cards[num])

    def ShowCards(self):
        for i in self.DeckToPlay:
            print(i)
        print(len(self.DeckToPlay),' карт')

    def HandOverCard(self):     #Процедура раздачи очередной карты
        global CurrentCardInDeckNum

        while True:
            CurrentCardInDeckNum += 1   #счетчик порядкового номера карты в колоде
            if CurrentCardInDeckNum<=51:
                yield self.DeckToPlay[CurrentCardInDeckNum-1]
            else:                       #если колода закончилась, а приходит очередной запрос на сдачу карты
                print('ВНИМАНИЕ!!! Колода закончилась!!!')
                yield False
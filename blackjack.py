from Deck import Deck
from Dealer import Dealer
from Player import Player
from GameUtilites import *
from GlobalVarNames import *   # файл с глобальными переменными в игре

#------------------------------------------------------------------------------------------------
def Start_New_Game():      #Выставляем настройки заново перед началом нового раунда
    global CurrentCardInDeckNum, moves
    CurrentCardInDeckNum = 0  # Обнуляем порядковый номер карты в колоде (перед началом новой игры)
    dealer.score=0          #обнуляем очки у дилера
    player.score=0          #обнуляем очки у игрока
    deck.ShuffleDeck()      #Тасуем колоду (перед началом новой игры)
    player.StartCards()     #Обнуляем набор карт у игрока (перед началом новой сдачи карт)
    dealer.StartCards()     #Обнуляем набор карт у дилера (перед началом новой сдачи карт)
    dealer.IsStand=player.IsStand=False #Переводим индикатор выбора "stand" у обоих игроков в положение False
    player.Hit(deck)        #Сдаем 1-ую карту игроку
    player.Hit(deck)        #Сдаем 2-ую карту игроку
    dealer.Hit(deck)        #Сдаем карту дилеру
    moves=0
#------------------------------------------------------------------------------------------------
def Whose_choice_is_now():  #функция, подчситывающая ходы в игре и определяющая, чей сейчас ход

    global moves
    while True:
        moves += 1  # счетчик ходов
        yield 'dealer'
        moves += 1  # счетчик ходов
        yield 'player'

#------------------------------------------------------------------------------------------------
def GameContinue():     #Процедура запроса у игрока продолжения игры. True - если продолжаем
    Right_Input=False
    while Right_Input==False:
        try:
            Player_Input=input('Хотите продолжить игру? 1-Да // 2-нет  ')
            if Player_Input in ('1','2'):
                Right_Input = True
                if Player_Input == '1':
                    return True
                elif Player_Input == '2':
                    return False
            else:
                raise ValueError

        except ValueError:
            print('Выбор не распознан. Попробуйте еще раз')

#------------------------------------------------------------------------------------------------
def Show_Result_Game():         #Процедура вывода на экран победителя матча
    if (player.score>21 and dealer.score>21) or (player.score==dealer.score):
        res='Draw'
    elif (player.score==21 and dealer.score!=21) or (player.score<=21 and dealer.score>21) or (player.score>dealer.score and player.score<=21):
        res='Player won'
    else:
        res='Player lost'
    TextToShow='___'+res
    print(TextToShow)
    WriteLog(LogFileName, TextToShow, False)
    WriteLog(LogFileName, '', False)    #вставляем пустую строку-разделитель в лог-файл

#------------------------------------------------------------------------------------------------
deck=Deck()     #Заводим экземпляр колоды
player=Player('player') #Заводим игрока в игру
dealer=Dealer('dealer')

WriteLog(LogFileName, '',True)    #очищаем лог-файл для записи и вставляем пустую строку-разделител


while not EndOfGame:
    Start_New_Game()          #тусуем колоду и делаем первичную раздачу карт
    player.RequireForPlayerBet()    #запрашиваем размер ставки в игре
    participant = Whose_choice_is_now() #определитель, чей чейчас ход

    player.ShowBet()  # выводим ставку игрока
    player.ShowCards()  # показываем карты игрока
    dealer.ShowCards()  # показываем карты дилера

    while (player.IsStand==False or dealer.IsStand==False) and (player.score!=21):
        name=next(participant)   #переход хода

        if name=='player':          #если ход игрока
            if player.IsStand:
                print("PLAYER'S MOVE: stand")
                WriteLog(LogFileName, "PLAYER'S MOVE: stand",False)
            else:
                player.Move(deck)

        if name=='dealer':          #если ход дилера
            if dealer.IsStand:
                print("DEALER'S MOVE: stand")
                WriteLog(LogFileName, "DEALER'S MOVE: stand", False)
            else:
                dealer.Move(deck)

        player.ShowBet()    #выводим ставку игрока
        player.ShowCards()  #показываем карты игрока
        dealer.ShowCards()  #показываем карты дилера

    print('***Game finish***')               #Вывод результатов матча
    print('RESULTS:')
    WriteLog(LogFileName, "")
    WriteLog(LogFileName, "***Game finish***")
    WriteLog(LogFileName, "RESULTS:")
    player.ShowScore()      #очки игрока
    dealer.ShowScore()      #очки дилера
    Show_Result_Game()      #результат матча

    if not GameContinue():  #Запрашиваем желание игрока пролжать игру
        EndOfGame=True      # Если игрок не хочет продолжать переводим индикатор окончания игры в положение True
        print('Игра окончена')


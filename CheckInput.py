def Check_input(func, mode='int', AllowZeroVal=False):      #Проверка введенного значения пользователем (Должно быть числовое значение от 0 и выше) и перевод его в тип float
    def inner(*args, **kwargs):
            RightInput = False
            while RightInput==False:
                Input_Val=func(*args)
                try:
                    if mode=='int':
                        Input_Val=int(Input_Val)
                    else:
                        Input_Val = float(Input_Val)

                    if Input_Val<0 or (Input_Val<=0 and AllowZeroVal==False):
                        raise ValueError
                    else:
                        RightInput = True
                except ValueError:
                    if AllowZeroVal==False:
                        print('Введенное значение должно быть числовым и строго больше нуля. Попробуйте еще раз')
                    else:
                        print('Введенное значение должно быть числовым от 0 и выше. Попробуйте еще раз')
            return Input_Val
    return inner



@Check_input
def AskForInput(text):      #Процедура, которая запрашивает значение у пользователя и делает его на проверку на тип Int и ненулевое значение
    Input_Val = input(text)

    return Input_Val
def WriteLog(FileName, data, new_file=False):      #процедура, которая делает лог-записи datd в файл с имененм FileName

    try:
        if new_file:            #если требуется начать новую запись файла (по умолчанию продолжаем вести старый файл
            with open(FileName, 'w', encoding='UTF8', newline='') as file:
                file.write(data+ '\n')
        else:
            with open(FileName, 'a', encoding='UTF8', newline='') as file:
                print(data, file=file)

    except Exception as e:
        print(f"Запись логов не произошла. Тип ошибки: {type(e).__name__}, сообщение: {str(e)}")


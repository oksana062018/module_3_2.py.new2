def send_email(message, recipient , sender = "university.help@gmail.com"):
    if ('@' and ".com" or ".ru" or ".net") not in (recipient or sender) or ("@" or (".com" or ".ru" or ".net")) not in (recipient or sender) :
        print (f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient == sender:
        print (f"Нельзя отправить письмо самому себе!")
    elif sender == 'university.help@gmail.com':
        print (f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")
send_email('Проверка связи', 'university@gmail.com')
send_email('Hello','university.help@gmail.com', '@.com')
send_email('Вы  лучший студент курса!', 'university.help@mail.ru')
send_email("_", 'university@gmail.co')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru')
send_email('Зачёт', 'university.help@gmail.com', sender='university.help@gmail.com')


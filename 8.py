def greet():
    return "Привет! Как я могу помочь вам?"

def inquire_status():
    return "Все хорошо, спасибо! А у вас как дела?"

def say_goodbye():
    return "Пока! Хорошего дня!"

def default_response():
    return "Простите, я не понимаю. Можете повторить?"

def process_message(message):
    responses = {
        'привет': greet,
        'как дела': inquire_status,
        'пока': say_goodbye
    }

    for keyword, response_function in responses.items():
        if keyword in message.lower():
            return response_function()

    return default_response()

while True:
    user_input = input("Введите ваше сообщение: ")
    if user_input.lower() == 'выход':
        print("До свидания!")
        break
    else:
        bot_response = process_message(user_input)
        print("Бот:", bot_response)

import datetime
import random


SUPPORTED_MOUTHS = ['января']

SUPPORTED_DAYS = {
    'января': ['первое', 'второе', 'третье', 'четвёртое', 'пятое', 'шестое', 'седьмое']
}


def main_skill(request, answer):
    # Кодить тут: request - запрос к нам, answer - то, что мы ответим
    # ------------------------------------------------------------------------
    if 'этот день в истории ' not in request['request']['command'].lower():
        answer['response']['text'] = f'Некорректный запрос'
        answer['response']['tts'] = answer['response']['text']
        answer['response']['end_session'] = True
        return answer

    date = request['request']['command'].lower().split('этот день в истории ')[1]
    day, month = date.split()

    if month not in SUPPORTED_MOUTHS or day not in SUPPORTED_DAYS[month]:
        answer['response']['text'] = f'Дата {date} не внесена в мою базу данных'
        answer['response']['tts'] = answer['response']['text']
        answer['response']['end_session'] = True
        return answer

    answer['response']['text'] = random.choice(open('events/' + date + '.txt').read().split('\n<EVENT>\n'))
    answer['response']['tts'] = answer['response']['text']
    answer['response']['end_session'] = True
    # ------------------------------------------------------------------------
    return answer

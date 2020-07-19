import datetime
import random
import os

import db_session
from db_user_class import User


MONTHS = {
    'января': 1,
    'февраля': 2,
    'марта': 3,
    'апреля': 4,
    'мая': 5,
    'июня': 6,
    'июля': 7,
    'августа': 8,
    'сентября': 9,
    'октября': 10,
    'ноября': 11,
    'декабря': 12
}

DAYS = {
    'первое': 1,
    'второе': 2,
    'третье': 3,
    'четвёртое': 4,
    'пятое': 5,
    'шестое': 6,
    'седьмое': 7,
    'восьмое': 8,
    'девятое': 9,
    'десятое': 10,
    'одиннадцатое': 11,
    'двенадцатое': 12,
    'тринадцатое': 13,
    'четырнанадцатое': 14,
    'пятнадцатое': 15,
    'шестнадцатое': 16,
    'семнадцатое': 17,
    'восемнадцатое': 18,
    'девятнадцатое': 19,
    'двадцатое': 20,
    'двадцать первое': 21,
    'двадцать второе': 22,
    'двадцать третье': 23,
    'двадцать четвёртое': 24,
    'двадцать пятое': 25,
    'двадцать шестое': 26,
    'двадцать седьмое': 27,
    'двадцать восьмое': 28,
    'двадцать девятое': 29,
    'тридцатое': 30,
    'тридцать первое': 31
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

    all_days = os.listdir('data/events')

    if date + '.txt' not in all_days:
        answer['response']['text'] = f'Дата {date} не внесена в мою базу данных'
        answer['response']['tts'] = answer['response']['text']
        answer['response']['end_session'] = True
        return answer

    db_session.global_init('data/users.db')
    session = db_session.create_session()

    user_id = request['session']['user_id']

    cur_user = session.query(User).filter(User.id == user_id).all()

    if not cur_user:
        cur_user = User(user_id)
    else:
        cur_user = cur_user[0]

    date_times = cur_user.date_times.split()
    month = MONTHS[month]
    day = DAYS[day]

    cur_day_number = (month - 1) * 31 + (day - 1)
    cur_day_times = int(date_times[cur_day_number])
    cur_day_events = open('data/events/' + date + '.txt').read().split('\n<EVENT>\n')

    answer['response']['text'] = random.choice(open('data/starts.txt').read().split('\n<START>\n')) + ' ' + \
                                 cur_day_events[cur_day_times % len(cur_day_events)] + \
                                 ' ' + random.choice(open('data/ends.txt').read().split('\n<END>\n'))
    answer['response']['tts'] = answer['response']['text']
    answer['response']['end_session'] = True

    cur_day_times += 1

    date_times[cur_day_number] = str(cur_day_times)

    cur_user.date_times = ' '.join(date_times)
    session.add(cur_user)
    session.commit()

    # ------------------------------------------------------------------------
    return answer

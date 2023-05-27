"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""


import random
import uuid
import datetime

import lorem

from pprint import pprint


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


def max_text_user(messages):
    message_counter = {}
    for message in messages:
        message_counter[message['sent_by']] = message_counter.setdefault(
            message['sent_by'], 0) + 1
    for key, value in message_counter.items():
        if value == max(message_counter.values()):
            return key


def most_repliable_user(messages):
    replies_counter = {}
    message_vs_user = {}

    for message in messages:
        message_vs_user[message['id']] = message['sent_by']

    for message in messages:
        if message['reply_for']:
            replies_counter[message_vs_user[message['reply_for']]] = replies_counter.setdefault(
                message_vs_user[message['reply_for']], 0) + 1

    for key, value in replies_counter.items():
        if value == max(replies_counter.values()):
            return key


def max_seen_users(messages, qty=3):
    users_seen = {}
    for message in messages:
        users_seen[message['sent_by']] = users_seen.setdefault(
            message['sent_by'], set([])).union(set(message['seen_by']))
    return list(dict(sorted(users_seen.items(), key=lambda item: len(item[1]), reverse=True)).keys())[:qty]


def most_active_time(messages):
    active_time = {
        'утром': 0,
        'днём': 0,
        'вечером': 0
    }
    for message in messages:
        hour = int(message['sent_at'].strftime('%H'))
        if hour < 12:
            active_time['утром'] += 1
        elif hour > 18:
            active_time['вечером'] += 1
        else:
            active_time['днём'] += 1

    for key, value in active_time.items():
        if value == max(active_time.values()):
            return key

def most_popular_starters(messages, qty=3):
    starters = {}
    for message in messages:
        if message['reply_for'] is None:
            starters[message['id']] = [message['id']]
        else:
            for value in starters.values():
                if message['reply_for'] in value:
                    value.append(message['id'])
                    break
    return list(dict(sorted(starters.items(), key=lambda item: len(item[1]), reverse=True)).keys())[:qty]


if __name__ == "__main__":
    # print(generate_chat_history())
    messages = generate_chat_history()
    print(
        f'Больше всего сообщений отправил пользователь: {max_text_user(messages)}.')
    print(
        f'Больше всего отвечали на сообщения пользователя: {most_repliable_user(messages)}.')
    print(
        f'Топ 3 пользователя с максимальным количество просмотров: {max_seen_users(messages)}.')
    print(
        f'Больше всего сообщений было отправлено {most_active_time(messages)}.')
    print(
        f'Топ 3 сообщения с самыми длинными тредами: {most_popular_starters(messages)}.')

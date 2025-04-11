import asyncio
from pyrogram import Client
import schedule
import time

api_id = ''  # Ваш API ID
api_hash = '' # API HASH
message_g = "" # Ваше сообщение

#path_to_chat_ids = '' # путь до файла chat_ids.txt

async def send_messages():
    print("Starting send_messages")
    async with Client('my_new_account', api_id, api_hash) as app:
        try:
            with open('chat_ids.txt', 'r') as f:
                links = [line.strip() for line in f]
        except Exception as e:
            print(f"Failed to read chat links. Error: {e}")
            return

        for link in links:
            username = link.split('/')[-1]  # извлекаем username из ссылки
            try:
                await app.send_message(username, message_g)  # <-- используем await
                print(f"Сообщение отправлено в чат {username}")
            except Exception as e:
                print(f"Ошибка в отправке сообщения {link}. Error: {e}")

    print("Все сообщения отправлены")

# Планировщик для запуска асинхронной функции
def schedule_task():
    asyncio.run(send_messages())  # <-- Запускаем асинхронный цикл

# Вызываем сразу и планируем отправку каждые 10 минут
schedule_task()
schedule.every(10).minutes.do(schedule_task)

while True:
    schedule.run_pending()
    time.sleep(1200)

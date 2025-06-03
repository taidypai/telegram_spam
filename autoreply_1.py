
from telethon.sync import TelegramClient, events
# Ваши данные из my.telegram.org
api_id = ''  # Ваш API ID
api_hash = ''

# 2. Текст ответа
AUTO_REPLY_TEXT = "Привет"

# 3. Подключение к аккаунту
client = TelegramClient('user_session', api_id, api_hash)

# 4. Обработчик входящих сообщений
@client.on(events.NewMessage(incoming=True))
async def reply_to_message(event):
    # Игнорируем групповые чаты (если нужно)
    if not event.is_private:
        return
    
    # Отправляем ответ
    await event.reply(AUTO_REPLY_TEXT)
    print(f"Ответил пользователю {event.sender_id}")

# 5. Запуск
print("Автоответчик запущен...")
client.start()
client.run_until_disconnected()
# telegram_spam

Приветствую всех, мой скрипт осуществляет спам рассылку в чаты Telegramm.

# Логика

 Вы подключаетесь к серверам telegram с помощью api. С помощью командной строки вам нужно будет зайти в ваш акаунт (Одноразового), после чего создаться сессия. 
 Скрипт возьмет чаты из файла chat_ids.txt и отправит с задержкой в час каждое сообщение.

 Настройка частоты отправки сообщений, можете изменить в строчке 42

     time.sleep(1200) 

Создание асинхронности, нужно для того чтобы вы смогли сразу использовать скрипт в своих работах отдельным потоком.

 

 

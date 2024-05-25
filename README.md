# Чат бот -New_SF_ConVeteR_Bot- 
Телеграм бот показывает конвертацию валюты. База данных сторонний API.
Обмены - exchanges: 
1. 'доллар':'USD'
2. 'евро':'EUR'
3. 'рубль':'RUB'
  

# описание:
1. При командах /start /help пользователю отправляется краткая информация о том, как пользоваться ботом;
2. При команде /values пользователю отправляется сообщение со списком доступных валют для конвертирования;
3. При вводе текста в формате: <имя валюты, цену которой хотим узнать> <имя валюты, в которой надо узнать цену первой валюты> <количество переводимой валюты>
- Пример №1: доллар евро 100. 
- Пример №2: доллар рубль 1,99. 
- Пример №3: евро рубль 1.99.
4. Пользователю отправляется сообщение с результатом конвертирования. Заданной волюты.
5. Сообщения об ошибках (например введена неправильная или несуществующая валюта или неправильно введено число) также отправляются пользователю.
6. Парсинг (requests json) для получения курса валют осуществляется через API сайта https://currencylayer.com/documentation. Тариф бесплатный, поэтому кол-во запросов - 1000 в месяц.

# Расположение файлов:
1. Бот и его функции - app.py
2. Классы и исключения - extensions.py
3. Токен бота API и переменные с длинным текстом - config.py

# Русский (Russian)
Задание: Написать Telegram-бота, в котором будет реализован следующий функционал:

Бот возвращает цену на определённое количество валюты (евро, доллар или рубль).
При написании бота необходимо использовать библиотеку pytelegrambotapi.
Человек должен отправить сообщение боту в виде <имя валюты, цену которой он хочет узнать> <имя валюты, в которой надо узнать цену первой валюты> <количество первой валюты>.
При вводе команды /start или /help пользователю выводятся инструкции по применению бота.
При вводе команды /values должна выводиться информация о всех доступных валютах в читаемом виде.
Для получения курса валют необходимо использовать любое удобное API и отправлять к нему запросы с помощью библиотеки Requests.
Для парсинга полученных ответов использовать библиотеку JSON.
При ошибке пользователя (например, введена неправильная или несуществующая валюта или неправильно введено число) вызывать собственно написанное исключение APIException с текстом пояснения ошибки.
Текст любой ошибки с указанием типа ошибки должен отправляться пользователю в сообщения.
Для отправки запросов к API описать класс со статическим методом get_price(), который принимает три аргумента и возвращает нужную сумму в валюте:
имя валюты, цену на которую надо узнать, — base;
имя валюты, цену в которой надо узнать, — quote;
количество переводимой валюты — amount.
Токен Telegram-бота хранить в специальном конфиге (можно использовать .py файл).
Все классы спрятать в файле extensions.py.

# English (Английский)
Task Write a Telegram bot that will implement the following functionality:

The bot returns the price for a certain amount of currency (euro, dollar or ruble).
When writing a bot, you need to use the pytelegrambotapi library.
A person should send a message to the bot in the form of .
When entering the /start or /help command, the user is shown instructions for using the bot.
When entering the /values command, information about all available currencies should be displayed in a readable form.
To get the exchange rate, you need to use any convenient API and send requests to it using the Requests library.
To parse the received responses, use the JSON library.
If a user makes an error (for example, an incorrect or non-existent currency is entered or a number is entered incorrectly), call the ApiException exception that is actually written with the error explanation text.
The text of any error indicating the type of error should be sent to the user in messages.
To send API requests, describe a class with a static get_price() method that takes three arguments and returns the required amount in currency:
the name of the currency to find out the price for — base;
the name of the currency, the price in which you need to find out, — quote;
the amount of currency to be transferred — amount.
The Telegram bot token is stored in a special config (you can use a .py file).
Hide all classes in a file extensions.py .


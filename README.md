# Telegram Tenor Parser Bot
## Описание
Это бот для телеграм ,который позволит парсить все gif из Tenor по запросу.<br>
Бот плохо работает в группах из за ограничений телеграм.
## Управление ботом
Для управления есть всего лишь 2 команды **/start [запрос]** допустим **/start коты** и команда **/stop** ,которая просто останавливает парсинг.
## Как запустить
Для начала скачиваем конечно же,дальше вам потребуется получить ключ Tenor <a href="https://developers.google.com/tenor/guides/quickstart">инструкция по получению тут</a> 
и ключ телеграм бота ,для этого пишем в телеграм боту <a href="https://t.me/BotFather">**BotFather**</a>.
После того как всё получили вводим ключи в соответствующие поля в файле **.env** .
Далее переходим в **main.py** и указываем в массив **allows** свой/и айди,которые смогут управлять ботом.Свой айди можно получить у <a href="https://t.me/getmyid_bot">**этого бота**</a>.

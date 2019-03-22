# LogServer

GET /last-upgrade - этот запрос возвращает дату последней
установки системных обновлений (т. е. apt-get upgrade / apt-get
dist-upgrade) как unix timestamp. Формат возвращаемых данных - JSON.

Парсим лог /var/log/apt/history.log

Приложить Dockerfile для запуска приложения в контейнере на основе Ubuntu 18.04


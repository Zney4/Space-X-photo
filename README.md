# Загрузка фотографий SpaceX

## Короткое описание проекта

```apod_image.py, epic_image.py, spacex_images.py``` - При запуске этих кодов будут устанавливаться фотографии с космосом (по отдельному).

```dowload_image_space.py``` - файл отвечающий за загрузку фотографий.


## Требования к окружению
Python

Python3 должен быть уже установлен,
затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей.
```python
pip install -r requirements.txt
```

## Переменные окружения
Файл .env      
В нём надо указать переменную с api токеном.
```
NASA_API_KEY=example
```

Для работы бота
```
TELEGRAM_BOT_TOKEN=example
TELEGRAM_CHAT_ID=example
```
1. Чтобы получить токен для бота нам нужно обратиться к BotFather в Телеграме: https://t.me/BotFather.
2. Нам нужно узнать chat_id собеседника с помощью этого бота: https://t.me/LeadConverterToolkitBot.

Api токен можно получить на этом сайте: https://app.bitly.com/https://api.nasa.gov/

## Примеры запуска кода

#### Для запуска скрипта(загрузка фото) - apod_image.py
```
python apod_image.py
```
Лучшее фото от NASA.

#### Для запуска скрипта(загрузка фото) - epic_image.py
```
python epic_image.py
```
Фотографии NASA нашей планеты.

#### Для запуска скрипта(загрузка фото) - spacex_images.py
```
python spacex_images.py
```
Фотографии с сайта SpaceX.

#### Для запуска телеграмм бота - SPACE_BOT.py
```
python SPACE_BOT.py
```

### Пример результата

Запускаем файл python dowload_image_space.py, после чего
создается папка image, в которую скачиваются изображения с космосом.

Эти изображение использует телеграм бот - SPACE BOT.py.
Он публикует изображении в бесконечном цикле и выбирает случайное фото, которое находиться в папке image раз в 4 часа.


## Телеграм бот, который реализует эти коды

```
SPACE BOT.py
```




Бот в бесконечном цикле публикует случайное фото, которое находиться в папке image раз в 4 часа.



### Цель проекта

Код написан в образовательных целях..

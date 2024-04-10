# Загрузка фотографий SpaceX

## Короткое описание проекта
SpaceX_photo.py - это код, который скачивает фотографии с сайта SpaceX.

## Требования к окружению
Python

Python3 должен быть уже установлен,
затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей.
```python
pip install -r requirements.txt
```

## Переменные окружения
Файл .env      
В нём надо указать перменую с api токеном.
```
API_TOKEN=example
```

Api токен можно получить на этом сайте: https://app.bitly.com/](https://api.nasa.gov/

## Пример запуска кода
```
python api.py --url bit.ly/3w4XIZ9
```

### Пример результата
```
Создается папка image, в которую скачиваются изображения с космосом.
```

## Телеграм бот, который релизует этот код
```
SPACE BOT.py
```
Бот в бесконечном цикле публикует случайное фото, которое находиться в папке image раз в 4 часа.



### Цель проекта

Код написан в образовательных целях.ъ.

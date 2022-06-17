# DjangoNotes
## Описание
Веб-приложение для создания заметок
## Запуск
Установить зависимости
```bash
pip install requirements.txt
```
Сделать миграции
```bash
python manage.py makemigrations
python manage.py migrate
```
Скачать и разархивировать библиотеки в каталог Notes/static/libs: https://drive.google.com/file/d/1P3EejmkCHcorKSUHHc-mEcgS2Tqdfp-X/view?usp=sharing

Собрать статические файлы
```bash
python manage.py collectstatic
```
Запустить с помощью
```bash
python manage.py runserver
```

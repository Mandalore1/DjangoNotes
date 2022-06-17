# DjangoNotes
## Описание
Веб-приложение для создания заметок
## Запуск
Установить зависимости
```bash
pip install -r requirements.txt
```
Сделать миграции
```bash
python manage.py makemigrations
python manage.py migrate
```
Скачать и разархивировать библиотеки в каталог Notes/static/libs: https://drive.google.com/file/d/1mV6W4xatTi22DvJd-y17kIpZ0h0CzqM-/view?usp=sharing

Собрать статические файлы
```bash
python manage.py collectstatic
```
Запустить с помощью
```bash
python manage.py runserver
```
## Скриншоты
### Список записок
![2022-06-17_17-02-27](https://user-images.githubusercontent.com/38291314/174294540-e5a9c41c-e668-4297-96e9-69353955189f.png)
### Создание записки
![Screenshot_20220617_164314](https://user-images.githubusercontent.com/38291314/174293226-9fdeff89-1a4d-4172-99c3-08500673789b.png)
### Информация о записке
![Screenshot_20220617_164334](https://user-images.githubusercontent.com/38291314/174293245-83bbc024-dea0-4449-b1e7-f8ecc2c4d81e.png)
### Информация о пользователе
![Screenshot_20220617_164344](https://user-images.githubusercontent.com/38291314/174293254-6b486db5-d73c-4375-a3d7-810d8b24695c.png)
### Редактирование информации о пользователе
![Screenshot_20220617_164358](https://user-images.githubusercontent.com/38291314/174293260-67dc0420-4048-4537-bcd3-c3001d8e6a6f.png)

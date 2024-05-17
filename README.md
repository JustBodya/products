ПРОДУКТЫ ФРУКТЫ И ОВОЩИ

ИНСТРУКЦИЯ ЗАПУСКА ВЕБ СЕРВЕРА ЛОКАЛЬКО:

скачайте проект через:
git clone

установите вирутальную среду:
python -m venv venv

запустите виртуальную среду:
.\venv\Scripts\activate

Установите нужные библиотеки:
pip install pip-tools
pip-compile.exe
pip install -r requirements.txt

Совершите миграции баз данных:
python manage.py makemigration
python manage.py migrate

Создайте админ пользователя
python manage.py createsuperuser

Запустите сервер локально:
python manage.py runserver


Суперпользователь(поставщик) имеет право добавлять продукты и выбирать их категорию. Обновлять продукты, а так же удалять.
Так же после создания суперпользователя через терминал, можно на сранице выйти log out, а так же зайти обратно через log in

Обычный пользователь, может только просматривать на странице продукты.

http://127.0.0.1:8000/admin/  административная панель
http://127.0.0.1:8000/api/v1/product/   список продуктов, а также создание продукта для админа
http://127.0.0.1:8000/api/v1/product/<int:pk>/   определенный продукт, а также обновление продукта для админа
http://127.0.0.1:8000/api/v1/productdelete/<int:pk>/  удаление продукта для админа
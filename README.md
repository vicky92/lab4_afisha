Необходимые компоненты: python 2.7, Ubuntu 12.04 и выше.

Установка необходимых зависимостей.
sudo apt-get install git
sudo apt-get install postgresql-9.3
sudo pip install Django 
sudo pip install psycopg2


Развертывание системы.

git clone https://github.com/vicky92/lab4_afisha.git
cd lab4_afisha
puthon manage.py syncdb
python manage.py runserver

Доступ к сайту: http://localhost:8000


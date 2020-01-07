Welcome to the Electronic Voting System. Initial setup:

1) set up a virtual enviroment
mkdir project
virtualenv myenv
pip install -r requirements .txt

2) start server
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

3) enjoy our app

regards,
Mihai and Andreea

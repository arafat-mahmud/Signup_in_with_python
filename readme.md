rm -rf env
python3 -m venv env
source env/bin/activate
pip install django
cd project
python3 manage.py runserver


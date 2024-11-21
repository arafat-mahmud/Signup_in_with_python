rm -rf env
python3 -m venv env
source env/bin/activate
pip install django
cd project
python3 manage.py runserver



# DEBUG = False if css is not working- 
python manage.py collectstatic
python manage.py runserver --insecure

# ensure Debug = true. 
# urls.py add:
# if settings.DEBUG:
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

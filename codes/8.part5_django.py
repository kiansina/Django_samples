## Django features and libraries, part 1


## wiping out your database
"""
. Sometimes you want to clear out and re-initialize your db-sqlite3 file
. The superusers and users are stored in the database so when you remove it, you need to re-create the super users.
"""

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
# choose user name password and email


# add a path to the code that gives us login and logout urls

#/home/sinakhan/django_projects/mysite/mysite/urls.py
path('accounts/',include('django.contrib.auth.urls')),

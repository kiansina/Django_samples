'''
In this assignment, you will build a web site that is roughly equivalent to
https://chucklist.dj4e.com/m1

This web site is a classified ad web site. People can view ads without logging in and if they log in, they can create
their own ads. It uses a social login that allows logging in using github accounts.

You will build this application by borrowing parts and pieces from the code that runs
https://samples.dj4e.com/
and combining them into a single application.

Make sure to get the latest version of dj4e-samples. If you have never checked it out on PythonAnywhere:
'''
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$:
cd ~
git clone https://github.com/csev/dj4e-samples
/$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

'''
If you have already checked dj4e-samples on PythonAnywhere do:
'''

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$:
workon django3     # or django3 if needed
cd ~/dj4e-samples
git pull
pip3 install -r requirements3.txt   # or requirements3.txt if needed
python manage.py check
/$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

'''
If you want to see requirements4.txt in git hub go to following link:
https://github.com/csev/dj4e-samples/blob/main/requirements4.txt
'''

"""
To switch to using the MySQL database outside of the PythonAnywhere, you might need to install the MySQL client and
possibly the server on your system before pip install will work using instructions at
https://pypi.org/project/mysqlclient/
- once you have the MySQL prerequisites installed or are using PythonAnywhere, you can run:
"""

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$:
pip3 install mysqlclient==1.4.6
/$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

"""
So your Python code can connect to MySQL databases. If you are having installation problems, you can keep using the
SQLite database but it will mean that your application will start to run much more slowly as we add complexity to
the application. It is especially to switch to MySQL on PythonAnywhere.

Important Note: If you find you have a problem saving files in the PythonAnywhere system using their browser-based
editor, you might need to turn off your ad blocker for this site - weird but true.
"""


#### Pulling In Code From Samples:

"""
In this section, we will break and then fix your settings.py and urls.py. When this is done, the autos, cats, dogs,
etc will stop working unless you add them back to these two files. It is OK for these applications not to be working.
The autograder will just look at /ads.

The files before changing are copied in 9.1 file and 9.2 files.

(1) Copy the settings.py and urls.py files and the entire home folder from the dj4e-samples project:
"""

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$:
cp ~/dj4e-samples/dj4e-samples/settings.py ~/django_projects/mysite/mysite
cp ~/dj4e-samples/dj4e-samples/urls.py ~/django_projects/mysite/mysite
cp -r ~/dj4e-samples/home/* ~/django_projects/mysite/home
/$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

"""
(2) Edit ~/django_projects/mysite/mysite/settings.py and then delete all the INSTALLED_APPLICATIONS after home.
You will have to search and replace dj4e-samples with mysite in a few places. Also set the name of your application
in the settings.py file to something other than ChucksList:
"""


# Used for a default title
APP_NAME = 'ChucksList'

"""
This shows up in default page titles and default page navigation.

(3) Edit your django_projects/mysite/mysite/urls.py and remove all of the path() calls to the sample applications.
Make sure to keep the path() to home.urls. Also keep the site and favicon rules in your urls.py.

(4) Edit the file django_projects/mysite/home/templates/home/main.html and replace the contents with this:
"""

{% extends "base_bootstrap.html" %}
{% block content %}
    <h1>Welcome to {{ settings.APP_NAME }}</h1>
    <p>
    Hello world.
    </p>
{% endblock content %}


"""
(5) At this point, you should be able to run:
"""

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$:
python manage.py check
/$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

"""
Keep running check until it does not find any errors.

If you get an error like Could not import github_settings.py for social_django when running manage.py or restarting
your PythonAnywhere webapp, don't worry - you will see this warning until you set up the social login.

If you are running on your local computer, (i.e not using PythonAnywhere) you can skip to step 9, otherwise continue
with these steps. Steps 6-8 are for PythonAnywhere.
"""


"""
(6) We are going to switch your application on PythonAnywhere from using an SQLite database to a MySQL database for
the rest of this course. If you keep running SQLite and your application stores too much data it will start to slow
down. If you are running locally, you can keep using SQLite.

(7) To use MySQL, first go to the Databases tab in PythonAnywhere. Make a MySQL database named ads and choose a name
and password and write them down.

(8) Edit ~/django_projects/mysite/mysite/settings.py and find the existing value for the DATABASES variable and
comment it out.
"""

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


"""
Add an entry to point Django at your newly created MySQL database. In this example, your PythonAnywhere account is
drchuck and the database you created is ads and the password you set for the database is phone_8675309. Change the
sample values below to the values for your database.
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sinakhan$ads',
        'USER': 'sinakhan',
        'PASSWORD': 'geshSIHTIR',
        'HOST': 'sinakhan.mysql.pythonanywhere-services.com',
         'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}


"""
(9) Once check works you will need to run your migrations and make a new administrator account:
"""


$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$:
cd ~/django_projects/mysite
python manage.py makemigrations      # Might say "no changes"
python manage.py migrate
python manage.py createsuperuser
/$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

username: dj4e_user1
Email: skr_e@yahoo.com
pass: Meow_8c9131_41


$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$:
python manage.py createsuperuser
/$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

username: dj4e_user2
Email: skr_e@yahoo.com
pass: Meow_42_8c9131


"""
If the makemigrations works and migrate fails, you may have an error in the DATABASE section of your settings.py.
You can edit your settings.py and rerun the migrate until it works.

Somtimes migrations or makemigrations takes up to a few minutes - if they are running and not showning any errors -
please be patient. If the migrations process is interrupted - you might need to drop your MySQL tables and run the
migrations again - instructions are shown below to drop the databases tables so you can run the migrations on a
fresh database.
"""


"""
(10) If you restart your web application, there won't be many working urls. Try these two to see if you have the
home code working properly:
"""

https://your-account.pythonanywhere.com/
https://your-account.pythonanywhere.com/favicon.ico
https://your-account.pythonanywhere.com/accounts/login


"""
Look at how pretty the login form looks :). Don't worry about the social login yet. We will get to that later.
Favicons are shown in the browser tabs. We will get to favicons later too :)
"""

#### Building the Ads Application

"""
In this section, you will pull bits and pieces of the sample applications repository and pull them into your ads
application.

Important Note: If you find you have a problem saving files in the PythonAnywhere system using their browser-based
editor, you might need to turn off your ad blocker for this site - weird but true.

(1) Create a new ads application within your mysite project:
"""

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$:
cd ~/django_projects/mysite
python manage.py startapp ads
/$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

"""
Then add the application to your mysite/mysite/settings.py and mysite/mysite/urls.py.

(2) Use this in your ads/model.py:
"""

from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings

class Ad(models.Model) :
    title = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    text = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        return self.title

"""
(3) Copy the owner.py from myarts to your ads application. This is the one file you do not have to change at all
(thanks to object orientation 😊).
"""


"""
(4) The files admin.py, views.py, urls.py, and the templates in the myarts folder will require significant
adaptation to be suitable for a classified ad application and the above model. A big part of this assignment is to
use the view classes that are in owner.py and used in views.py. The new owner field should not be shown to the user
on the create and update forms, it should be automatically set by the classes like OwnerCreateView in owner.py. If
you see an "owner" drop down in your create screen the program is not implemented correctly and will fail the
autograder.
"""


"""
(5) Adapt the templates in myarts/templates/myarts as a starting point to create the needed templates in
ads/templates/ads.
"""

"""
(6) When you are implementing the update and delete views, make sure to follow the url patterns for the update and
delete operations. They should be of the form /ad/14/update and /ad/14/delete. Something like the following should
work in your urls.py:
"""

from django.urls import path, reverse_lazy
from . import views

app_name='ads'
urlpatterns = [
    path('', views.AdListView.as_view(), name='all'),
    path('ad/<int:pk>', views.AdDetailView.as_view(), name='ad_detail'),
    path('ad/create',
        views.AdCreateView.as_view(success_url=reverse_lazy('ads:all')), name='ad_create'),
    path('ad/<int:pk>/update',
        views.AdUpdateView.as_view(success_url=reverse_lazy('ads:all')), name='ad_update'),
    path('ad/<int:pk>/delete',
        views.AdDeleteView.as_view(success_url=reverse_lazy('ads:all')), name='ad_delete'),
]


"""
(7) As you build the application, use check periodically as you complete some of the code.
"""


$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$:
python manage.py check
/$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

"""
(8) Once your application is mostly complete and can pass the check without error, add the new models to your
migrations and database tables:
"""

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$:
python manage.py makemigrations
python manage.py migrate
/$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$



#### Debugging: Searching through all your files in the bash shell

''''
If you have errors, you might find the grep tool very helpful in figuring out where you might find your errors.
For example, lets say after you did all the editing, and went to the ads url and got this error:
'''

NoReverseMatch at /ads
'myarts' is not a registered namespace

"""
You thought you fixed all the instances where the string "myarts" was in your code, but you must have missed one.
You can manually look at every file individually or use the following command to let the computer do the searching:
"""

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$:
cd ~/django_projects/mysite
grep -ri myarts *
/$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


"""
You might see output like this:
"""

ads/templates/ads/ad_list.html:<a href="{% url 'login' %}?next={% url 'myarts:all' %}">Login</a>

"""
The grep program searches files in the current folder and subfolders for any lines in any file that have the string
"myarts" in them and shows you the file name and the line it is mentioned.

The grep command is the "Generalized Regular Expression Parser" and is one of the most useful Linux commands to know.
The 'r' means 'recursive' and the 'i' means 'ignore case. The grep program will save you so much time 😊.
"""

#### Adding the Bootstrap menu to the top of the page

"""
Next we will add the bootstrap navigation bar to the top of your application as shown in:

https://chucklist.dj4e.com/

This top bar includes a 'Create Ad' navigation item and the login/logout navigation with gravatar when the user
logs in.

(1) Edit all four of the ads_ files in ads/templates/ads to change them so they extend ads/base_menu.html. Change
the first line of each file from:
"""

{% extends "base_bootstrap.html" %}

"""
to be:
"""

{% extends "base_menu.html" %}

"""
(2) Then create home/templates/base_menu.html with the following content:
"""

{% extends "base_bootstrap.html" %}
{% block navbar %}
{% load app_tags %}
<nav class="navbar navbar-default navbar-inverse">
  <div class="container-fluid">
    <div class="navbar-header">
        <a class="navbar-brand" href="/">{{ settings.APP_NAME }}</a>
    </div>
    <!-- https://stackoverflow.com/questions/22047251/django-dynamically-get-view-url-and-check-if-its-the-current-page -->
    <ul class="nav navbar-nav">
      {% url 'ads' as ads %}
      <li {% if request.get_full_path == ads %}class="active"{% endif %}>
          <a href="{% url 'ads:all' %}">Ads</a></li>
    </ul>
    <ul class="nav navbar-nav navbar-right">
        {% if user.is_authenticated %}
        <li>
        <a href="{% url 'ads:ad_create' %}">Create Ad</a>
        </li>
        <li class="dropdown">
            <a href="#" data-toggle="dropdown" class="dropdown-toggle">
                <img style="width: 25px;" src="{{ user|gravatar:60 }}"/><b class="caret"></b>
            </a>
            <ul class="dropdown-menu">
                <li><a href="{% url 'logout' %}?next={% url 'ads:all' %}">Logout</a></li>
            </ul>
        </li>
        {% else %}
        <li>
        <a href="{% url 'login' %}?next={% url 'ads:all' %}">Login</a>
        </li>
        {% endif %}
    </ul>
  </div>
</nav>
{% endblock %}


"""
(3) Find the line in your base_bootstrap.html that looks like this:
"""

<meta name="dj4e-code" content="99999999">

"""
and change the 9999999 to be "42166900907178"

Make sure to check the autograder for additional markup requirements.

When you are done, you should see an 'Ads' menu on the left and a 'Create Ad' link on the right just like the sample
implementation.
"""

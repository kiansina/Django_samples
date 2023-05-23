# Create a crud app
# https://www.dj4e.com/assn/dj4e_autos.md?PHPSESSID=d733dedc29a6d8aba092b71806a22b46
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$:
mkvirtualenv django3 #if necessary
workon django3
cd ~/django_projects/mysite
python manage.py startapp autos
/$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""
Since we will build a number of applications in this project, we will use the home application to provide convienent urls to
switch between applications.

And you should have a file mysite/home/templates/home/main.html that has the text for the top-level page. You can keep the
"Hello World" text in the page somewhere.

Add a link to the "/autos" url in mysite/home/templates/home/main.html and anything else the autograder needs:
"""

<li><a href="/autos">Autos CRUD</a>


$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$:
cd dj4e-samples
git pull

"""
Create mysite/home/templates/registration folders using mkdir and copy the (login.html) template from dj4e-samples into
mysite/home/templates/registration/login.html.
"""

"""
Copy the file from dj4e-samples/home/templates/base_bootstrap.html into your mysite/home/templates - this will be used in your
autos/templates and make our HTML look better by applying the Bootstrap and other styling libraries.
"""

"""
Edit mysite/mysite/settings.py add the autos application to the list of INSTALLED_APPS. You can follow the pattern of the
HomeConfig line in that file.
"""

"""
Edit mysite/mysite/urls.py and add the accounts/ path so you can use the Django built in login features. (Authentication Views).
Also edit mysite/mysite/urls.py to route autos/ urls to autos/urls.py file.
"""

path('accounts/', include('django.contrib.auth.urls')),  # Add
path('autos/', include('autos.urls')),                   # Add

"""
Edit the autos/views.py file to add views for the list, create, update, and delete views for both autos and makes based on the
sample code.
"""

# Sample repository :
# https://github.com/csev/dj4e-samples/tree/main/autos

"""
Edit the autos/urls.py file to add routes for views for both autos and makes
"""

"""
In your views.py file, you can start out using the Make views from the sample code, but once you have the application working,
you should come back and rewrite the Make views using the same patterns as the Auto views. If you switch to the pattern in the
Autos views and use the generic edit views on your Make views you no longer need to have a MakeForm or forms.py. You can either
write the long version of the views or the short version of the views - the short version is easier to code but more challenging
to understand because it relies so heavily on a complex parent object and inheritance.
"""

"""
Run the python manage.py check until you see no errors
"""

"""
Run the python manage.py makemigrations until it has no errors. Sometimes when you make changes to models.py, the makemigrations
will pick up on the changes and ask you for example if you want to rename a field. Sometimes you make a change to your models.py
and makemigrations gets stuck or lost. If migrations gets stuck, you might need to start with a fresh database.
"""

"""
Run the python manage.py migrate to create the database
"""

"""
Edit autos/admin.py to add the Auto and Make models to the Django administration interface.
"""

"""
Run the python manage.py check until you see no errors
"""

"""
Create a superuser so you can test the admin interface and log in to the application.
"""

"""
Create the necessary template files in autos/templates/autos to support your views.
Note that the the second sub folder under templates is there to make sure that templates
are not inadvertently shared across multiple applications within a Django project.
"""

"""
Find the line in your base_bootstrap.html that looks like this:
"""

<meta name="dj4e-code" content="99999999">

"""
and change the 9999999 to be "42166479304938"

Make sure to check the autograder for additional markup requirements.
"""

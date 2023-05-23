## Writing your first Django app, part 2


## Database setup
"""
Now, open up mysite/settings.py. It’s a normal Python module with module-level variables
representing Django settings.

By default, the configuration uses SQLite. If you’re new to databases, or you’re just
interested in trying Django, this is the easiest choice. SQLite is included in Python,
so you won’t need to install anything else to support your database. When starting your
first real project, however, you may want to use a more scalable database like PostgreSQL,
to avoid database-switching headaches down the road.

If you wish to use another database, install the appropriate database bindings and change
the following keys in the DATABASES 'default' item to match your database connection
settings:

ENGINE – Either 'django.db.backends.sqlite3', 'django.db.backends.postgresql',
'django.db.backends.mysql', or 'django.db.backends.oracle'. Other backends are
also available.

NAME – The name of your database. If you’re using SQLite, the database will be a file on
your computer; in that case, NAME should be the full absolute path, including filename,
of that file. The default value, BASE_DIR / 'db.sqlite3', will store the file in your
project directory.

If you are not using SQLite as your database, additional settings such as USER, PASSWORD,
and HOST must be added. For more details, see the reference documentation for DATABASES.
"""
#https://docs.djangoproject.com/en/3.2/ref/settings/#std-setting-DATABASES

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'mydatabase',
#        'USER': 'mydatabaseuser',
#        'PASSWORD': 'mypassword',
#        'HOST': '127.0.0.1',
#        'PORT': '5432',
#    }
#}



"""
For databases other than SQLite

If you’re using a database besides SQLite, make sure you’ve created a database by
this point. Do that with “CREATE DATABASE database_name;” within your database’s
interactive prompt.

Also make sure that the database user provided in mysite/settings.py has “create database”
privileges. This allows automatic creation of a test database which will be needed in a
later tutorial.

If you’re using SQLite, you don’t need to create anything beforehand - the database
file will be created automatically when it is needed.
"""

"""
While you’re editing mysite/settings.py, set TIME_ZONE to your time zone.
"""




"""
Also, note the INSTALLED_APPS setting at the top of the file. That holds the names of all
Django applications that are activated in this Django instance. Apps can be used in multiple
projects, and you can package and distribute them for use by others in their projects.

By default, INSTALLED_APPS contains the following apps, all of which come with Django:

django.contrib.admin – The admin site. You’ll use it shortly.
django.contrib.auth – An authentication system.
django.contrib.contenttypes – A framework for content types.
django.contrib.sessions – A session framework.
django.contrib.messages – A messaging framework.
django.contrib.staticfiles – A framework for managing static files.
These applications are included by default as a convenience for the common case.

Some of these applications make use of at least one database table, though, so we need to
create the tables in the database before we can use them. To do that, run the following
command:
"""

$ python3 manage.py migrate

##Creating models
"""
Now we’ll define your models – essentially, your database layout, with additional metadata.
"""

"""
Philosophy

A model is the single, definitive source of information about your data. It contains the
essential fields and behaviors of the data you’re storing. Django follows the DRY Principle.
The goal is to define your data model in one place and automatically derive things from it.

This includes the migrations - unlike in Ruby On Rails, for example, migrations are entirely
derived from your models file, and are essentially a history that Django can roll through to
update your database schema to match your current models.
"""

"""
In our poll app, we’ll create two models: Question and Choice. A Question has a question and
a publication date. A Choice has two fields: the text of the choice and a vote tally. Each
Choice is associated with a Question.

These concepts are represented by Python classes. Edit the polls/models.py file so it looks
like this:
"""

from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


##Activating models
"""
That small bit of model code gives Django a lot of information. With it, Django is able to:

Create a database schema (CREATE TABLE statements) for this app.
Create a Python database-access API for accessing Question and Choice objects.
But first we need to tell our project that the polls app is installed.
"""


"""
Philosophy

Django apps are “pluggable”: You can use an app in multiple projects, and you can distribute
apps, because they don’t have to be tied to a given Django installation.
"""


"""
To include the app in our project, we need to add a reference to its configuration class in
the INSTALLED_APPS setting. The PollsConfig class is in the polls/apps.py file, so its
dotted path is 'polls.apps.PollsConfig'. Edit the mysite/settings.py file and add that
dotted path to the INSTALLED_APPS setting. It’ll look like this:
"""

INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]



#Now Django knows to include the polls app. Let’s run another command:

$ python manage.py makemigrations polls



"""
There’s a command that will run the migrations for you and manage your database schema
automatically - that’s called migrate, and we’ll come to it in a moment - but first, let’s
see what SQL that migration would run. The sqlmigrate command takes migration names and
returns their SQL:
"""


$ python manage.py sqlmigrate polls 0001


"""
If you’re interested, you can also run python manage.py check; this checks for any problems
in your project without making migrations or touching the database.
"""


$ python manage.py check

#Now, run migrate again to create those model tables in your database:

$ python manage.py migrate



##!!!!!!!!!!!!!!!!!!!!!!!!!!! RECAP:
""""
for now, remember the three-step guide to making model changes:

Change your models (in models.py).
Run python manage.py makemigrations to create migrations for those changes
Run python manage.py migrate to apply those changes to the database.

"""




##Playing with the API
"""
Now, let’s hop into the interactive Python shell and play around with the free API Django
gives you. To invoke the Python shell, use this command:
"""

$ python manage.py shell

"""
We’re using this instead of simply typing “python”, because manage.py sets the
DJANGO_SETTINGS_MODULE environment variable, which gives Django the Python import path to
your mysite/settings.py file.

Once you’re in the shell, explore the database API:
"""

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BLOCK
>>> from polls.models import Choice, Question  # Import the model classes we just wrote.

# No questions are in the system yet.
>>> Question.objects.all()
<QuerySet []>

# Create a new Question.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
>>> q.save()

# Now it has an ID.
>>> q.id
1

# Access model field values via Python attributes.
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)

# Change values by changing the attributes, then calling save().
>>> q.question_text = "What's up?"
>>> q.save()

# objects.all() displays all the questions in the database.
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>]>
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BLOCK



"""
Wait a minute. <Question: Question object (1)> isn’t a helpful representation of this object.
Let’s fix that by editing the Question model (in the polls/models.py file) and adding
a __str__() method to both Question and Choice:
"""

from django.db import models

class Question(models.Model):
    # ...
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text

"""
It’s important to add __str__() methods to your models, not only for your own convenience
when dealing with the interactive prompt, but also because objects’ representations are used
throughout Django’s automatically-generated admin.
"""

#Let’s also add a custom method to this model:


import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

#Save these changes and start a new Python interactive shell by running python manage.py
#     shell again:


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BLOCK
>>> from polls.models import Choice, Question

# Make sure our __str__() addition worked.
>>> Question.objects.all()
<QuerySet [<Question: What's up?>]>

# Django provides a rich database lookup API that's entirely driven by
# keyword arguments.
>>> Question.objects.filter(id=1)
<QuerySet [<Question: What's up?>]>
>>> Question.objects.filter(question_text__startswith='What')
<QuerySet [<Question: What's up?>]>

# Get the question that was published this year.
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: What's up?>

# Request an ID that doesn't exist, this will raise an exception.
>>> Question.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Question matching query does not exist.

# Lookup by a primary key is the most common case, so Django provides a
# shortcut for primary-key exact lookups.
# The following is identical to Question.objects.get(id=1).
>>> Question.objects.get(pk=1)
<Question: What's up?>

# Make sure our custom method worked.
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True

# Give the Question a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a question's choice) which can be accessed via the API.
>>> q = Question.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
>>> q.choice_set.all()
<QuerySet []>

# Create three choices.
>>> q.choice_set.create(choice_text='Not much', votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text='The sky', votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)

# Choice objects have API access to their related Question objects.
>>> c.question
<Question: What's up?>

# And vice versa: Question objects get access to Choice objects.
>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
3

# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any question whose pub_date is in this year
# (reusing the 'current_year' variable we created above).
>>> Choice.objects.filter(question__pub_date__year=current_year)
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

# Let's delete one of the choices. Use delete() for that.
>>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
>>> c.delete()
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BLOCK


## Introducing the Django Admin
"""
Philosophy

Generating admin sites for your staff or clients to add, change, and delete content is
tedious work that doesn’t require much creativity. For that reason, Django entirely
automates creation of admin interfaces for models.

Django was written in a newsroom environment, with a very clear separation between “content
publishers” and the “public” site. Site managers use the system to add news stories, events,
sports scores, etc., and that content is displayed on the public site. Django solves the
problem of creating a unified interface for site administrators to edit content.

The admin isn’t intended to be used by site visitors. It’s for site managers.
"""

#Creating an admin user
"""
First we’ll need to create a user who can login to the admin site. Run the following
command:
"""

$ python manage.py createsuperuser
"""
Username: sena
email :sina.kian@mail.polimi.it
pass: *********
"""


## Start the development server
"""
The Django admin site is activated by default. Let’s start the development server and
explore it.

If the server is not running start it like so:
"""

$ python manage.py runserver

#Now, open a Web browser and go to “/admin/” on your local domain – e.g.,
#    http://127.0.0.1:8000/admin/. You should see the admin’s login screen


## Make the poll app modifiable in the admin
"""
But where’s our poll app? It’s not displayed on the admin index page.

Only one more thing to do: we need to tell the admin that Question objects have an admin
interface. To do this, open the polls/admin.py file, and edit it to look like this:
"""

from django.contrib import admin

from .models import Question

admin.site.register(Question)

# Again run following to see the changes:
$ python manage.py runserver

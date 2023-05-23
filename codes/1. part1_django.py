#Writing your first Django app, part 1


## Creating a project
"""
If this is your first time using Django, you’ll have to take care of some initial
setup. Namely, you’ll need to auto-generate some code that establishes a Django
project – a collection of settings for an instance of Django, including database
configuration, Django-specific options and application-specific settings.

From the command line, cd into a directory where you’d like to store your code,
then run the following command:
"""
#go to directory:
#first you should write following:
$ cd /mnt/c
# Then with cd
#           pwd
#           ls
#go to the file

$ sudo apt-get update #This solves the probable errors of the next command

$ django-admin startproject mysite

## The development server
"""
Let’s verify your Django project works. Change into the outer mysite directory,
if you haven’t already, and run the following commands:
"""
$ python3 manage.py runserver

## Changing the port
"""
By default, the runserver command starts the development server on the internal
IP at port 8000.

If you want to change the server’s port, pass it as a command-line argument. For
instance, this command starts the server on port 8080:
"""

$ python manage.py runserver 8080

"""
If you want to change the server’s IP, pass it along with the port. For example,
to listen on all available public IPs (which is useful if you are running Vagrant
or want to show off your work on other computers on the network), use:
"""
$ python manage.py runserver 0:8000

"""
0 is a shortcut for 0.0.0.0. Full docs for the development server can be found in
the runserver reference.
"""

## Automatic reloading of runserver
"""
The development server automatically reloads Python code for each request as needed.
You don’t need to restart the server for code changes to take effect. However, some
actions like adding files don’t trigger a restart, so you’ll have to restart the server
in these cases.
"""


## Projects vs. apps
"""
What’s the difference between a project and an app? An app is a Web application that
does something – e.g., a Weblog system, a database of public records or a small poll app.
A project is a collection of configuration and apps for a particular website. A project
can contain multiple apps. An app can be in multiple projects.
"""

"""
Your apps can live anywhere on your Python path. In this tutorial, we’ll create our poll
app in the same directory as your manage.py file so that it can be imported as its own
top-level module, rather than a submodule of mysite.

To create your app, make sure you’re in the same directory as manage.py and type this
command:
"""


$ python manage.py startapp polls
#That’ll create a directory polls whith other files such as admin.py etc.

## Write your first view
"""
Let’s write the first view. Open the file polls/views.py and put the following Python
code in it:
"""

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

"""
This is the simplest view possible in Django. To call the view, we need to map it
to a URL - and for this we need a URLconf.

To create a URLconf in the polls directory, create a file called urls.py.
"""
#in directory of .../polls/ create urls.py

"""
In the polls/urls.py file include the following code:
"""


from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

"""
The next step is to point the root URLconf at the polls.urls module. In mysite/urls.py,
add an import for django.urls.include and insert an include() in the urlpatterns list,
so you have:
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]


"""
The include() function allows referencing other URLconfs. Whenever Django encounters
include(), it chops off whatever part of the URL matched up to that point and sends
the remaining string to the included URLconf for further processing.

The idea behind include() is to make it easy to plug-and-play URLs. Since polls are
in their own URLconf (polls/urls.py), they can be placed under “/polls/”, or under
“/fun_polls/”, or under “/content/polls/”, or any other path root, and the app will
still work.
"""

##When to use include()
"""
You should always use include() when you include other URL patterns. admin.site.urls
is the only exception to this
"""

"""
You have now wired an index view into the URLconf. Verify it’s working with the following
command:
"""

$ python manage.py runserver


"""
Go to http://localhost:8000/polls/ in your browser, and you should see the text “Hello,
world. You’re at the polls index.”, which you defined in the index view.
"""

##Page not found?
"""
If you get an error page here, check that you’re going to http://localhost:8000/polls/
and not http://localhost:8000/.
"""

"""
The path() function is passed four arguments, two required: route and view, and two
optional: kwargs, and name. At this point, it’s worth reviewing what these arguments
are for.
"""

## path() argument: route
"""
route is a string that contains a URL pattern. When processing a request, Django
starts at the first pattern in urlpatterns and makes its way down the list, comparing
the requested URL against each pattern until it finds one that matches.

Patterns don’t search GET and POST parameters, or the domain name. For example, in a
request to
https://www.example.com/myapp/,
the URLconf will look for myapp/.
In a request to
https://www.example.com/myapp/?page=3, the URLconf will also look for myapp/.
"""


## path() argument: view
"""
When Django finds a matching pattern, it calls the specified view function with an
HttpRequest object as the first argument and any “captured” values from the route as
keyword arguments. We’ll give an example of this in a bit.
"""


## path() argument: kwargs
"""
Arbitrary keyword arguments can be passed in a dictionary to the target view. We aren’t
going to use this feature of Django in the tutorial.
"""


##path() argument: name
"""
Naming your URL lets you refer to it unambiguously from elsewhere in Django, especially
from within templates. This powerful feature allows you to make global changes to the URL
patterns of your project while only touching a single file.

When you’re comfortable with the basic request and response flow, read part 2 of this
tutorial to start working with the database.
"""

# DJANGO NOTES

following tutorial(s) here:
https://www.youtube.com/watch?v=rHux0gMZ3Eg

https://www.youtube.com/watch?v=F5mRW0jo-U4

## Reference

https://docs.djangoproject.com/en/4.0/intro/overview/

## Setup

start new virtual environment using pipenv inside the current project folder (will automatically go into .venv folder if it exists)

`mkdir .venv`

`pipenv install django`

to build venv from requirements.txt file in main dir

`pipenv install -r requirements.txt`

lauch virtual env

`.venv/Scripts.activate.bat`

to freeze packages and generate requirements.txt

`pip freeze > requirements.txt`

start django project in current folder - suggest putting django project in src subfolder below current virtual environment

`django-admin startproject project-name . `

create new app - will make a subfolder with template files

`python manage.py startapp appname`

create admin user

`python manage.py createsuperuser`

## Common tasks

make migrations from models created/updated in code

`python manage.py makemigrations`

run migrations

`python manage.py migrate`

open python shell with access to models etc.

`python manage.py shell`

run server on default port 8000

`python manage.py runserver`

run server in background at host ip address, on port 8000 and 

`nohup python manage.py runserver 0.0.0.0:8000 &`

to kill off a running server instance - find pid by searching for instances of runserver then kill that pid

`ps auxw | grep runserver`
`kill pid`

### actions/requests
* Django calls these views, but they are really action/request handlers
* Django calls views templates
* functions in 'views.py' should be methods that take requests and return django.http.HttpResponse objects
* entries look like this: 

`path('hello/', views.say_hello)`

### url route mapping
* create 'urls.py' in the specific app subfolder
* create a list called 'urlpatterns' with django.urls.path entries that link a path to a method in 'views.py'
* also update the urlpatterns list in the main project to include the app-specific url config
* use like this: 

`path('blog/', include('blog.urls'))`

### views/templates
* called template in Django but actually a view (HTML markup)
* store in 'templates' subfolder under app subfolder
* use django.shortchuts.render to return HTTP responses like this: 

`return render(request, template_name='hello.html')`

* use context argument to map string values to python objects like this: 

`render(request, template_name='hello.html', context={'name': 'James'})`

* and in the HTML template use double braces to access: 

`<h1>Hello {{ name }} from the template</h1>`

* in the template do if statements like so: 

`{% if name %}`

`   <p>Hello {{ name }} from the template</p>`

`{% else %}`

`   <p>Hello World from the template</p>`

`{% endif %}`

* can use generic tag {% block content_name %}  {% endblock %} to bulk replace HTML content on a template page
* need to place inside a default page called 'base.html'
* at the top of subsequent pages use {% extends 'base.html' %}

### interactive debugging
* create a launch.json file with the Django style template
* can specify port 9000 as optional arg so it doesn't clash with other server instance
* can add debugging breakpoints and step into/over code lines
* run application with debugging F5
* run application without debugging CTRL+F5


### Django Debug toolbar
* install django-debug-toolbar using pipenv or conda
* add 'debug_tollbar' to list of installed apps in 'settings.py'
* add url pattern to 'url.py'
* add debug_toolbar to middleware in 'settings.py' at the top of the list
* add internal ip address to INTERNAL_IPS in 'settings.py' 
* reference: https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
* debugging toolbar will appear as sidebar in browser when an HTML page is returned


### ORM in Django
* association class = join table for many to many relationships
* table names created from class name e.g. `class Product(models.Model)`
* use model fields to create DB attributes e.g. `title = models.TextField()`
* register models in 'admin.py' to look at them in the admin interface 
* create a sub-method in the model called __str__ that returns a particular attribute if you would like that to show up when viewing the model instances in the admin viewer/shell
* reference for field types https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-types
* most fields allow null=, default=, blank= options - sometime necessary when making updates
* null keyword enforces at the DB level
* blank keyword enforces at the user creation level (does not affect existing records in DB)

```
from .models import Product
admin.site.register(Product)
```

* accessing/creating model instances in shell terminal
```
python manage.py shell
from playground.models import Product
Product.objects.all()
Product.objects.create(title='some title', description='desc', price='20', summary='sweet')
```


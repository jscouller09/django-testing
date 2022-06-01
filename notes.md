# DJANGO NOTES

following tutorial here:
https://www.youtube.com/watch?v=rHux0gMZ3Eg

## Setup

start django project in current folder

`django-admin startproject project-name . `

run server on default port 8000

`python manage.py runserver`

create new app - will make a subfolder with template files

`python manage.py startapp appname`

## Common tasks

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
from django.urls import path
from .views import (
    CourseView,
    CourseListView,
    CourseCreateView,
)

# URLConf
app_name = 'courses'
urlpatterns = [
    path('', CourseListView.as_view(), name='course-list'),
    path('<int:id>/', CourseView.as_view(), name='course-detail'),
    path('create/', CourseCreateView.as_view(), name='course-create'),
]

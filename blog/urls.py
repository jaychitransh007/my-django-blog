# Here we're importing Django's function path and all of our views from the blog application
from django.urls import path
from . import views

# As you can see, we're now assigning a view called post_list to the root URL
urlpatterns = [
    path('', views.post_list, name='post_list'),
]

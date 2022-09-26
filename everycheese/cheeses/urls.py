# everycheese/cheeses/urls.py
from django.urls import path
from . import views


app_name = "cheeses"
urlpatterns = [
    path(
        route='',
        view=views.CheeseListView.as_view(),
        name='list'
    ),
    path(
        route='<slug:slug>/',
        view=views.CheeseDetailView.as_view(),
        name='detail'
    ),
]

# to make this work have to add it in root URLConf. 
# go to config/urls.py and add after your stuff custom urls includes go here comment 
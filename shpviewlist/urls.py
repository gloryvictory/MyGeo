from django.urls import path
from . import views


urlpatterns = [
    path('', views.shpviewlist, name='shpviewlist')
]

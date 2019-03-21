from django.urls import path
from . import views


urlpatterns = [
    path('', views.comp_list_view, name='comp_list_view')
]

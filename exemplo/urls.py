from django.urls import path

from exemplo import views

app_name = 'exemplo'

urlpatterns = [
    path('', views.ClienteList.as_view(), name='list'),
]
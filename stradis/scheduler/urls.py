from django.urls import path

from . import views
    
app_name = 'scheduler'

urlpatterns = [
    path('', views.index, name='index'),
    path('schedule', views.schedule, name='schedule')
]
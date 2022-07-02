from django.urls import path, re_path
from . import views

from django.conf.urls.static import static

app_name = 'NightOut'

urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('create_event', views.create_event, name='create_event'),
    path('event_list', views.event_list, name='event_list'),
    path('event_list/voting/<pk>', views.voting, name='voting'),

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

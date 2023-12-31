from django.urls import path, include

from . import views

app_name = 'core'
urlpatterns = [
    path('', views.core_view),
    path('about/', views.core_about, name='about'),
    path('signin/', views.core_signin, name='signin'),
    path('signup/', views.core_signup, name='signup'),
]
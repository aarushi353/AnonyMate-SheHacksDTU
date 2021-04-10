from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('', views.home, name="home"),
    path('chat/', views.chat, name="chat"),
    path('chatting/', views.chatting, name="chatting"),
    path('faq/', views.Faq, name="Faq"),
    path('guide/', views.guide, name="guide"),
    path('sign/', views.sign, name="sign"),
    path('home/', views.home, name="home"),
]

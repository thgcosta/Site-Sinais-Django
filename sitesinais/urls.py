from django.urls import path

from sitesinais import views

app_name = 'sitesinais'

urlpatterns = [
    path('', views.home, name="home"),
    path('cadastro/', views.cadastro, name="cadastro"),
    path('my-page/', views.trial, name="trial"),
    path('confirmacao/', views.confirmacao, name="confirmacao"),
]
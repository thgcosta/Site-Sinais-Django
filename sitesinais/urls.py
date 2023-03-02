from django.urls import path

from sitesinais import views

app_name = 'sitesinais'

urlpatterns = [
    path('', views.home, name="home"),
    path('cadastro/', views.cadastro, name="cadastro"),
    path('my-page/', views.trial, name="trial"),
    path('confirmacao/', views.confirmacao, name="confirmacao"),
    path('logout/', views.logout_view, name="logout"),
    path('api-last-14/', views.get_last_results, name="get_last_results"),
    path('api-signal/', views.get_signal, name="get_signal"),
]

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sitesinais.urls')),  # inclui os links do aplicativo ao diretorio '/'
]

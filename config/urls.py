from django.contrib import admin
from django.urls import include, path
from links.views import health
urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health)
]

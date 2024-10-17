from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('greeting/', include('greeting_app.urls')),
    path('admin/', admin.site.urls),
]

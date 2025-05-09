from django.contrib import admin
from django.urls import path, include
import website.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('website/', include(website.urls))
]

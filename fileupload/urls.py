
from django.contrib import admin
from django.urls import path
from upload.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('upload/', upload)
]

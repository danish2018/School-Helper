from django.contrib import admin
from django.urls import path
from main.views import search_school_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', search_school_view, name='your_view'),
]

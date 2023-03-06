from django.contrib import admin
from django.urls import include, path

from . import views
from mySite.mysite import home
from mysite.views import home

urlpatterns = [
        path('polls/', include('polls.urls')),
        path('admin/', admin.site.urls),
        path('', home),
        ]



from django.contrib import admin
from django.urls import include, path

from . import views
# from mySite.mysite import home
from . import views
from . views import home

urlpatterns = [
        path('polls/', include('polls.urls')),
        path('admin/', admin.site.urls),
        path('', home),
        # path('', views.home()),
        ]



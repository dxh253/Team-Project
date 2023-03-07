from django.contrib import admin
from django.urls import include, path

# from mySite.mysite import home
from . views import homepage, helpSection

urlpatterns = [
        # path('polls/', include('polls.urls')),
        # path('admin/', admin.site.urls),
        path('', homepage),
        ]


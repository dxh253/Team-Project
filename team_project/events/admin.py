from django.contrib import admin
from .models import Category, Events, UserEvent

admin.site.register(Category)
admin.site.register(Events)
admin.site.register(UserEvent)

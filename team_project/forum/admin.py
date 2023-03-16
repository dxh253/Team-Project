from django.contrib import admin
from .models import Forum, Post, Thread

admin.site.register(Forum)
admin.site.register(Post)
admin.site.register(Thread)

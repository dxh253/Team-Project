from django.contrib import admin
from .models import Category, Post, PostVotes, PostComment

# Register your models here.
class MyClassAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified', 'slug')

class MyChildren(admin.ModelAdmin):
    readonly_fields = ('children', )

admin.site.register(Category, MyClassAdmin)
admin.site.register(Post, MyClassAdmin)
admin.site.register(PostVotes)
admin.site.register(PostComment, MyChildren)
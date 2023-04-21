from django.contrib import admin
from . import models
class MyClassAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified', 'slug')

class MyChildren(admin.ModelAdmin):
    readonly_fields = ('children', )

admin.site.register(models.Category)
admin.site.register(models.Post)
admin.site.register(models.PostVotes)
admin.site.register(models.Comment)
admin.site.register(models.Reply)

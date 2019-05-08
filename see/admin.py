from django.contrib import admin
from .models import Profile,Post,Comment

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','prof_pic','bio')

admin.site.register(Profile,ProfileAdmin)
admin.site.register(Post)
admin.site.register(Comment)

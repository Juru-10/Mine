from django.contrib import admin
from .models import Profile,Image,Follow

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','prof_pic','bio')

admin.site.register(Profile,ProfileAdmin)
admin.site.register(Image)
admin.site.register(Follow)

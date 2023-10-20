from django.contrib import admin
from .models import User

@admin.register(User)
class Useradmin(admin.ModelAdmin):
    list_display=['id','name','email','password']

# admin.site.register(User)
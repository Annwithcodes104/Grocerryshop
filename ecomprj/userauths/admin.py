from django.contrib import admin

from userauths.models import User

class UseAdmin(admin.ModelAdmin):
    list_display=['username','email','bio']

# Register your models here.
admin.site.register(User,UseAdmin)
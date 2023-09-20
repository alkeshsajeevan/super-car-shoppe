from django.contrib import admin
from .models import  CarMake,CarModel,UserProfile

# Register your models here.
class CarMakeAdmin(admin.ModelAdmin):
    list_display=('name',)


class CarModelAdmin(admin.ModelAdmin):
    list_display=('make','name','year','price','is_sold')
   



admin.site.register(CarMake,CarMakeAdmin)
admin.site.register(CarModel,CarModelAdmin)

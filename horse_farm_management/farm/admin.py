from django.contrib import admin
from .models import Horse, Farm, Employee

class HorseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'breed', 'age')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'breed')
    list_filter = ('breed',)

class FarmAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'owner')
    list_display_links = ('id', 'name')
    search_fields =  ('id', 'name', 'location', 'owner')
    list_filter = ('owner','location')
    
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'farm')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'position', 'farm')
    list_filter = ('position', 'farm')

admin.site.register(Horse, HorseAdmin)
admin.site.register(Farm, FarmAdmin)
admin.site.register(Employee, EmployeeAdmin)

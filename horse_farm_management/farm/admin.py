from django.contrib import admin
from .models import Horse, Farm, Employee, TrainingSession

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
    list_display = ('id', 'name', 'position', )
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'position', )
    list_filter = ('position', )
    
class TrainingSessionAdmin(admin.ModelAdmin):
    list_display = ['horse', 'employee', 'date', 'duration']
    list_filter = ['date', 'horse', 'employee']

admin.site.register(Horse, HorseAdmin)
admin.site.register(Farm, FarmAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(TrainingSession, TrainingSessionAdmin)

from django.contrib import admin
from .models import Prosthetics, Reviews, Staff

# Register your models here.

@admin.register(Prosthetics)
class ProstheticsAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'name_uz', 'type_prosthetics_ru')
    list_filter = ('type_prosthetics_ru', 'status')
    search_fields = ('name_ru', 'name_uz', 'type_prosthetics_ru')


admin.site.register(Reviews)
admin.site.register(Staff)
from django.contrib import admin

from petstagram_last.pets.models import Pet




@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
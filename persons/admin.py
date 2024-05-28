from django.contrib import admin

from persons.models import Persons, Position, Skills


class PersonsAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age', 'position']
admin.site.register(Persons, PersonsAdmin)

admin.site.register(Position)
admin.site.register(Skills)

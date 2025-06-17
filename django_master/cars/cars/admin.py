from django.contrib import admin
from .models import Car
# Register your models here.


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'model_year', 'value', 'plate')
    search_fields = ('model', 'brand')


# admin.site.register(Car, CarAdmin)

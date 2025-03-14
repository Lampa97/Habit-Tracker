from django.contrib import admin
from .models import Habit

# Register your models here.

@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = "__all__"
    list_filter = "__all__"

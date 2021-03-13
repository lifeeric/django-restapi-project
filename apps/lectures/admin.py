from django.contrib import admin
from .models import Lecture


class LectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'lecturer_name', 'date')
    serach_fields = ('name', 'lecturer_name', )


admin.site.register(Lecture, LectureAdmin)

from django.contrib import admin
from .models import CourseManage


class CourseManageAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CourseManage._meta.get_fields()]


admin.site.register(CourseManage, CourseManageAdmin)

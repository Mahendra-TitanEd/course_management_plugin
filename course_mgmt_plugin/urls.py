"""
https://lms.example.edu/course_mgmt/api/v1/courses/
https://lms.example.edu/course_mgmt/dashboard
"""
# Django
from django.conf.urls import url

# this repo

from course_mgmt_plugin.courses.views import courses_list

app_name = "course_mgmt_plugin"

urlpatterns = [
    url(r"^api/v1/courses/?$", courses_list, name="courses-list"),
]

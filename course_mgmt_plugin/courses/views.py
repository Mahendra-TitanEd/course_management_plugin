import logging

from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie


log = logging.getLogger(__name__)


@login_required
@ensure_csrf_cookie
def courses_list(request):
    """
    example url:
    https://lms.example.edu/course_mgmt/api/v1/courses/
    """
    return redirect(reverse("dashboard"))

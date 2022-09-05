"""
Models for Course Management Information

Migration Notes

If you make changes to this model, be sure to create an appropriate migration
file and check it in at the same time as your model changes. To do that,

1. Go to the edx-platform dir
2. ./manage.py lms makemigrations --settings=production 
3. ./manage.py lms migrate --settings=production
"""
from django.db import models
from django.utils.translation import ugettext as _
from django.dispatch import receiver
from model_utils.models import TimeStampedModel

from xmodule.modulestore.django import SignalHandler

from openedx.core.djangoapps.content.course_overviews.models import CourseOverview


def get_or_none(classmodel, **kwargs):
    """
    Return object if exist otherwise return None
    """
    try:
        return classmodel.objects.get(**kwargs)
    except Exception as e:
        return None


class CourseManage(TimeStampedModel):
    """
    Model for store course releted extra details
    """

    course = models.OneToOneField(
        CourseOverview,
        db_constraint=False,
        db_index=True,
        on_delete=models.CASCADE,
    )
    product_id = models.CharField("Product ID", max_length=255, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.course_id)

    class Meta:
        verbose_name = "CourseManage"
        verbose_name_plural = "Course Management"

    @classmethod
    def create_or_update(cls, course_id, data_dict):
        """
        Create or update Course Details.
        """
        course, created = cls.objects.get_or_create(course_id=course_id)
        course.product_id = data_dict.get("product_id")
        course.save()


@receiver(SignalHandler.course_published)
def course_publish_signal_handler(sender, course_key, **kwargs):
    """
    Receives publishing signal and update it into course manage
    """

    course, created = CourseManage.objects.get_or_create(course_id=course_key)


@receiver(SignalHandler.course_deleted)
def _listen_for_course_delete(sender, course_key, **kwargs):  # pylint: disable=unused-argument
    """
    Catches the signal that a course has been deleted from Studio and
    invalidates the corresponding Course cache entry if one exists.
    """
    CourseManage.objects.filter(course_id=course_key).delete()

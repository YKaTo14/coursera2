"""App config for the OnlineCourse app."""

from django.apps import AppConfig


class OnlinecourseConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "onlinecourse"
    verbose_name = "OnlineCourse"

    def ready(self):
        from . import signals  # noqa: F401

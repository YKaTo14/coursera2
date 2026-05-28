"""URL routes for the OnlineCourse app."""

from django.urls import path

from . import views


app_name = "onlinecourse"

urlpatterns = [
    path("", views.course_details, name="course_details"),
    path("course/<int:course_id>/", views.course_details, name="course_details_by_id"),
    path("course/<int:course_id>/submit/", views.submit, name="submit"),
    path("result/<int:submission_id>/", views.show_exam_result, name="show_exam_result"),
]

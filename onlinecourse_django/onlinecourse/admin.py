"""Admin registrations for the OnlineCourse demo project."""

from django.contrib.admin import ModelAdmin, TabularInline
from django.contrib import admin

from .models import Choice, Course, Lesson, Question, Submission


class QuestionInline(TabularInline):
    model = Question
    extra = 1


class ChoiceInline(TabularInline):
    model = Choice
    extra = 2


class LessonAdmin(ModelAdmin):
    list_display = ("title", "course", "order")
    list_filter = ("course",)
    search_fields = ("title", "course__title")
    inlines = [QuestionInline]


class QuestionAdmin(ModelAdmin):
    list_display = ("text", "lesson", "order")
    list_filter = ("lesson__course",)
    search_fields = ("text", "lesson__title")
    inlines = [ChoiceInline]


class CourseAdmin(ModelAdmin):
    list_display = ("title", "slug")
    search_fields = ("title", "slug")


class SubmissionAdmin(ModelAdmin):
    list_display = ("course", "student_name", "score", "total_questions", "created_at")
    list_filter = ("course", "created_at")
    search_fields = ("student_name", "course__title")


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission, SubmissionAdmin)

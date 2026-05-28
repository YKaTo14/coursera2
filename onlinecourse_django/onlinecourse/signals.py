"""Seed demo content after migrations run."""

from django.db.models.signals import post_migrate
from django.dispatch import receiver

from .models import Choice, Course, Lesson, Question


@receiver(post_migrate)
def create_demo_content(sender, **kwargs):
    if sender.name != "onlinecourse":
        return

    course, _ = Course.objects.get_or_create(
        slug="mock-exam",
        defaults={
            "title": "Mock Exam for Django Online Course",
            "description": "A small demo course used to test the final project submission flow.",
        },
    )

    lessons = [
        {
            "order": 1,
            "title": "Django Basics",
            "content": "Learn how Django structures projects and apps.",
            "questions": [
                {
                    "order": 1,
                    "text": "What is Django?",
                    "choices": [
                        ("A high-level Python web framework", True),
                        ("A Java compiler", False),
                        ("A database engine", False),
                    ],
                },
            ],
        },
        {
            "order": 2,
            "title": "Templates and Forms",
            "content": "Render pages and send data back to the server.",
            "questions": [
                {
                    "order": 1,
                    "text": "Which HTTP method should a quiz form usually use when submitting answers?",
                    "choices": [
                        ("POST", True),
                        ("TRACE", False),
                        ("DELETE", False),
                    ],
                },
                {
                    "order": 2,
                    "text": "Which template tag links to a named URL pattern?",
                    "choices": [
                        ("url", True),
                        ("include", False),
                        ("static", False),
                    ],
                },
            ],
        },
    ]

    for lesson_data in lessons:
        lesson, _ = Lesson.objects.get_or_create(
            course=course,
            order=lesson_data["order"],
            defaults={
                "title": lesson_data["title"],
                "content": lesson_data["content"],
            },
        )
        for question_data in lesson_data["questions"]:
            question, _ = Question.objects.get_or_create(
                lesson=lesson,
                order=question_data["order"],
                defaults={"text": question_data["text"]},
            )
            for idx, (choice_text, is_correct) in enumerate(question_data["choices"], start=1):
                Choice.objects.get_or_create(
                    question=question,
                    text=choice_text,
                    defaults={"is_correct": is_correct},
                )

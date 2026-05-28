"""Views for the OnlineCourse demo project."""

from django.shortcuts import get_object_or_404, redirect, render

from .models import Choice, Course, Question, Submission


def get_demo_course():
    return Course.objects.prefetch_related("lessons__questions__choices").order_by("id").first()


def course_details(request, course_id=None):
    if course_id is None:
        course = get_demo_course()
    else:
        course = get_object_or_404(
            Course.objects.prefetch_related("lessons__questions__choices"),
            pk=course_id,
        )
    if course is None:
        return render(request, "onlinecourse/course_details_bootstrap.html", {"course": None})

    return render(request, "onlinecourse/course_details_bootstrap.html", {"course": course})


def submit(request, course_id):
    course = get_object_or_404(
        Course.objects.prefetch_related("lessons__questions__choices"),
        pk=course_id,
    )

    if request.method != "POST":
        return redirect("onlinecourse:course_details_by_id", course_id=course.id)

    questions = Question.objects.filter(lesson__course=course).select_related("lesson").prefetch_related("choices")
    score = 0
    answers = {}

    for question in questions:
        field_name = f"question_{question.id}"
        choice_id = request.POST.get(field_name)
        selected_choice = Choice.objects.filter(pk=choice_id, question=question).first() if choice_id else None
        correct_choice = question.choices.filter(is_correct=True).first()
        is_correct = bool(selected_choice and selected_choice.is_correct)
        if is_correct:
            score += 1
        answers[str(question.id)] = {
            "question": question.text,
            "selected_choice": selected_choice.text if selected_choice else "",
            "correct_choice": correct_choice.text if correct_choice else "",
            "is_correct": is_correct,
        }

    submission = Submission.objects.create(
        course=course,
        student_name=request.POST.get("student_name", "").strip(),
        score=score,
        total_questions=questions.count(),
        answers=answers,
    )
    return redirect("onlinecourse:show_exam_result", submission_id=submission.id)


def show_exam_result(request, submission_id):
    submission = get_object_or_404(
        Submission.objects.select_related("course").prefetch_related("course__lessons__questions__choices"),
        pk=submission_id,
    )
    questions = Question.objects.filter(lesson__course=submission.course).select_related("lesson").prefetch_related("choices")

    question_results = []
    for question in questions:
        answer_data = submission.answers.get(str(question.id), {})
        question_results.append(
            {
                "question": question,
                "selected_choice": answer_data.get("selected_choice", ""),
                "correct_choice": answer_data.get("correct_choice", ""),
                "is_correct": answer_data.get("is_correct", False),
            }
        )

    return render(
        request,
        "onlinecourse/exam_result.html",
        {
            "submission": submission,
            "question_results": question_results,
            "passed": submission.total_questions > 0 and submission.score == submission.total_questions,
        },
    )

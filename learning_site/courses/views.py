from itertools import chain
from django.shortcuts import render, get_object_or_404
from . import models

# Create your views here.
def course_list(request):
    courses = models.Course.objects.all()
    email = 'questions@learning-site.com'
    return render(request, 'courses/course_list.html', {'courses': courses, 'email': email})


def course_detail(request, pk):
    course = get_object_or_404(models.Course, pk=pk)
    steps = sorted(chain(course.text_set.all(), course.quiz_set.all()),
                   key=lambda step: step.order)
    print(steps)
    return render(request, 'courses/course_detail.html', {
        'course': course,
        'steps': steps,
        })

def text_detail(request, course_pk, step_pk):
    step = get_object_or_404(models.Text, course_id = course_pk, pk = step_pk)
    return render(request, 'courses/step_detail.html', {'step': step})


def quiz_detail(request, course_pk, step_pk):
    step = get_object_or_404(models.Quiz, course_id = course_pk, pk = step_pk)
    return render(request, 'courses/step_detail.html', {'step': step})

from django.shortcuts import render, get_object_or_404
from .models import Course, Step

# Create your views here.
def course_list(request):
    courses = Course.objects.all()
    email = 'questions@learning-site.com'
    return render(request, 'courses/course_list.html', {'courses': courses, 'email': email})


def course_detail(request, pk):
    # course = Course.objects.get(pk=pk)
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})

def step_detail(request, course_pk, step_pk):
    step = get_object_or_404(Step, course_id = course_pk, pk = step_pk)
    return render(request, 'courses/step_detail.html', {'step': step})

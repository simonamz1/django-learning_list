from django.urls import reverse
from django.test import TestCase
from django.utils import timezone
from .models import Course, Step

# Create your tests here.

class CourseModelTests(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
            title='Python Basics',
            description='Learning Python for beginners'
        )
        now = timezone.now()
        self.assertLess(course.created_at, now)

    def test_title_exist(self):
        course = Course.objects.create(
            title='Python Basics',
            description='Learning Python for beginners'
        )
        self.assertIn('Python', course.title)


class StepModelTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title='Python Basics',
            description='Learning Python for beginners'
        )
    def test_step_creation(self):
        step = Step.objects.create(
            title='Python functions',
            description='Syntax of python functions',
            course=self.course
        )
        self.assertIn(step, self.course.step_set.all())


class CourseViewsTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title='Python Testing',
            description='Learn to write tests in Python'
        )
        self.course2 = Course.objects.create(
            title='New Course',
            description='A new course'
        )
        self.step = Step.objects.create(
            title='Introduction to Doctests',
            description='Learn to write tests in your docstrings.',
            course=self.course
        )

    def test_course_list_view(self):
        # self.client acts like a web browser and lets you make requests to URLs, both inside and outside of your Django project
        resp = self.client.get(reverse('courses:course_list'))
        # checks that status_code of the response is equal to 200 (valide)
        self.assertEqual(resp.status_code, 200)
        # checks that the context of the response (context defined in the different views) is contained in the first parameter
        self.assertIn(self.course, resp.context['courses'])
        self.assertIn(self.course2, resp.context['courses'])
        # checks that a given template is used somewhere in the response view
        self.assertTemplateUsed(resp, 'courses/course_list.html')
        # checks that a given string is somewhere in the text of a response
        self.assertContains(resp, self.course.title)

    def test_course_detail_view(self):
        resp = self.client.get(reverse('courses:course', kwargs={'pk': self.course.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.course, resp.context['course'])

    def test_step_detail_view(self):
        resp = self.client.get(reverse('courses:step', kwargs={'course_pk': self.course.pk, 'step_pk': self.step.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.step, resp.context['step'])

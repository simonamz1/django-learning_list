from django import template
from courses.models import Course
from django.utils.safestring import mark_safe
import markdown2
register = template.Library()

@register.simple_tag
def newest_course():
    '''Gets the most recent course that was added to the library'''
    return Course.objects.latest('id')

@register.inclusion_tag('courses/course_nav.html')
def nav_courses_list():
    '''Returns dictionary of courses to display as navigation pane'''
    courses = Course.objects.all()
    return {'courses': courses}

@register.filter('time_estimate')
def time_estimate(word_count):
    '''Estimate the number of minutes it will take to complete a step based ont the passed-in wordcount'''
    minutes = round(word_count/20)
    return minutes

@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    '''Converts markdown text to HTML'''
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)

@register.simple_tag
def conjugate_is(num):
    if num == 1:
        return "is"
    else:
        return "are"

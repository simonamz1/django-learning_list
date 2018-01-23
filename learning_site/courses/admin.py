from django.contrib import admin

from .models import Course, Text, Quiz


class TextInline(admin.StackedInline):
    model = Text

class QuizInline(admin.StackedInline):
    model = Quiz

class CourseAdmin(admin.ModelAdmin):
    inlines = [TextInline, QuizInline,]


admin.site.register(Course, CourseAdmin)
admin.site.register(Text)
admin.site.register(Quiz)

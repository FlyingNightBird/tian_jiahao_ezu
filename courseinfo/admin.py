from django.contrib import admin
from .models import Semester, Section, Student, Course, Instructor, Period, Registration, Year

admin.site.register(Student)
admin.site.register(Semester)
admin.site.register(Section)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Period)
admin.site.register(Registration)
admin.site.register(Year)

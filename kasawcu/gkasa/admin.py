from kasawcu.gkasa.models import Student
from kasawcu.gkasa.models import Course
from kasawcu.gkasa.models import Requirement
from kasawcu.gkasa.models import Lab
from django.contrib import admin


class CoursesInline(admin.TabularInline):
    model = Course.student_id.through


class LabsInline(admin.TabularInline):
    model = Lab.student_id.through


class StudentAdmin(admin.ModelAdmin):
    inlines = [
    CoursesInline,
    LabsInline,
    ]


admin.site.register(Course)
admin.site.register(Requirement)
admin.site.register(Student, StudentAdmin)
admin.site.register(Lab)

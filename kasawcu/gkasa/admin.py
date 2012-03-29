from kasawcu.gkasa.models import Student
from kasawcu.gkasa.models import Course
from kasawcu.gkasa.models import Requirement 
from kasawcu.gkasa.models import Lab
from django.contrib import admin

class StudentsInline(admin.TabularInline): 
  model = Course.student_id.through

class StudentAdmin(admin.ModelAdmin):
  inlines = [
    StudentsInline,
  ]

class RequirementInline(admin.TabularInline):
  model = Requirement.course_id.through

class CourseAdmin(admin.ModelAdmin):
  inlines = [
    RequirementInline,
  ]

admin.site.register(Course, CourseAdmin)
admin.site.register(Requirement) 
admin.site.register(Student, StudentAdmin)
admin.site.register(Lab)

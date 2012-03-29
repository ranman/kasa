from django.db import models

# Create your models here.
class Student(models.Model):
  student_id = models.IntegerField(primary_key=True, unique=True,
      db_index=True, max_length=9) 
  first_name = models.CharField(max_length=50)
  last_name  = models.CharField(max_length=50)
  
  def __unicode__(self):
    return u"%s %s" % (self.first_name, self.last_name) 


class Course(models.Model):
  course_id = models.AutoField(primary_key=True, unique=True, 
                              db_index=True, max_length=4)
  title = models.CharField(max_length=50)
  dept = models.CharField(max_length=6)
  number = models.IntegerField(max_length=5) 
  student_id = models.ManyToManyField(Student, blank=True, through='StudentCourse')
  
  def __unicode__(self):
    return u"%s %s" % (self.dept, self.number)

class StudentCourse(models.Model):
  student = models.ForeignKey(Student)
  course = models.ForeignKey(Course)
  date_taken = models.DateField()

class Lab(models.Model):
  lab_id = models.AutoField(primary_key=True, unique=True, 
                              db_index=True, max_length=4)
  title = models.CharField(max_length=50)
  desc = models.CharField(max_length=500)
  student_id = models.ManyToManyField(Student, blank=True, through='StudentLab')

  def __unicode__(self):
    return u"%s" % (self.title)

class StudentLab(models.Model):
  student = models.ForeignKey(Student)
  lab = models.ForeignKey(Lab)
  date_take = models.DateField()

class Requirement(models.Model):
  req_id = models.AutoField(primary_key=True, unique=True, 
                            db_index=True, max_length=3)
  req_desc = models.CharField(max_length=500)
  title = models.CharField(max_length=500)
  course_id = models.ManyToManyField(Course, blank=True)
  lab_id = models.ManyToManyField(Lab, blank=True)

  def __unicode__(self):
    return u"%s" % (self.title)

# Create your views here.
from kasawcu.gkasa.models import *
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

def detail(request, student_id):
  s = get_object_or_404(Student, pk=student_id)
  c = Course.objects.filter(student_id=s.student_id)
  l = Lab.objects.filter(student_id=s.student_id) 
  r = Requirement.objects.get(Q(course_id__in=c) | Q(lab_id__in=l)) 
  return render_to_response('detail.html', 
                            {'student': s, 
                            'courses': c,
                            'labs': l,
                            'requirements': r},
                            context_instance=RequestContext(request))

def report(request, student_id):
  s = get_object_or_404(Student, pk=student_id)
  c = Course.objects.filter(student_id=s.student_id)
  l = Lab.objects.filter(student_id=s.student_id) 
  r = Requirement.objects.get(Q(course_id__in=c) | Q(lab_id__in=l)) 
  return render_to_response('result.html', 
                            {'student': s, 
                            'courses': c,
                            'labs': l,
                            'requirements': r},
                            context_instance=RequestContext(request))

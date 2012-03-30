# Create your views here.
from kasawcu.gkasa.models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

def detail(request):
  return render_to_response('detail.html')                            

@login_required
def report(request, student_id):
  s = get_object_or_404(Student, pk=student_id)
  c = Course.objects.filter(student_id=s.student_id)
  l = Lab.objects.filter(student_id=s.student_id) 
  r = Requirement.objects.filter(Q(course_id__in=c) | Q(lab_id__in=l)) 
  return render_to_response('result.html', 
                            {'student': s, 
                            'courses': c,
                            'labs': l,
                            'requirements': r},
                            context_instance=RequestContext(request))

# Create your views here.
from kasawcu.gkasa.models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext


def detail(request):
    return render_to_response('detail.html')


@login_required
def report(request, student_id):
    s = get_object_or_404(Student, pk=student_id)
    c = s.course_set.all().select_related()
    l = s.lab_set.all().select_related()
    r = Requirement.objects.filter(Q(course_id__in=c) | Q(lab_id__in=l)).distinct()
    n = Requirement.objects.exclude(req_id__in=r).select_related()
    return render_to_response('result.html',
                              {'student': s,
                              'courses': c,
                              'labs': l,
                              'requirements': r,
                              'needed': n},
                              context_instance=RequestContext(request))

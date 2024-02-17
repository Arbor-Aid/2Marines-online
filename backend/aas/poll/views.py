from django.shortcuts import get_object_or_404, render

from .models import Organization

def index(request):
    return render(request, 'poll/index.html', {})

def OrgView(request, org_id):
    org = get_object_or_404(Organization, pk=org_id)
    context = {
        'org': org,
    }
    return render(request, 'poll/org_view.html', context)

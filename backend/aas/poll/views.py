from django.shortcuts import get_object_or_404, render, redirect
from rest_framework import viewsets
from urllib.parse import urlparse

from .serializers import OrganizationSerializer

from .models import Organization

def index(request):
    return render(request, 'poll/index.html', {})

def OrgInputStart(request):
    return render(request, 'poll/org_input_start.html', {})

def OrgEdit(request, org_id = None):
    if org_id is not None:
        org = Organization.objects.get(pk=org_id)
    else:
        org = Organization()

    context = {
        'org': org,
    }
    return render(request, 'poll/org_view.html', context)

def OrgSearch(request):
    orgQuery = request.POST['organization']
    orgUrl = urlparse(orgQuery).hostname
    org = Organization.objects.get(website=orgUrl)
    if org:
        return redirect("/poll/edit/{id}/".format(id=org.id))
    else:
        return redirect("/poll/edit/")

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

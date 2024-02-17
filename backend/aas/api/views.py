from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from rest_framework import viewsets, generics
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
    try:
        org = Organization.objects.get(website=orgUrl)
    except Organization.DoesNotExist:
        return redirect("/poll/edit/")
    return redirect("/poll/edit/{id}/".format(id=org.id))

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class OrganizationByIdViewSet(generics.ListAPIView):
    serializer_class = OrganizationSerializer

    def get_queryset(self):
        org_id = self.kwargs['org_id']
        return Organization.objects.filter(id=org_id)

class OrganizationUpdateByIdViewSet(generics.UpdateAPIView):
    serializer_class = OrganizationSerializer

    def update(self, request, *args, **kwargs):
        org_id = self.kwargs['org_id']
        org = Organization.objects.get(id=org_id)
        org.name = org.name if 'name' not in request.data else request.data['name']
        org.description = org.description if 'description' not in request.data else request.data['description']
        org.address = org.address if 'address' not in request.data else request.data['address']
        org.county = org.county if 'county' not in request.data else request.data['county']
        org.phone = org.phone if 'phone' not in request.data else request.data['phone']
        org.email = org.email if 'email' not in request.data else request.data['email']
        org.website = org.website if 'website' not in request.data else request.data['website']
        org.appointment_required = org.appointment_required if 'appointment_required' not in request.data else request.data['appointment_required']
        org.for_whom = org.for_whom if 'for_whom' not in request.data else request.data['for_whom']
        org.save()
        return HttpResponse(status=204)

class OrganizationDeleteByIdViewSet(generics.DestroyAPIView):
    serializer_class = OrganizationSerializer

    def destroy(self, request, *args, **kwargs):
        org_id = self.kwargs['org_id']
        org = Organization.objects.get(id=org_id)
        org.delete()
        return HttpResponse(status=204)

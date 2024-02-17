from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from rest_framework import viewsets, generics
from urllib.parse import urlparse

from .serializers import OrganizationSerializer, HoursSerializer

from .models import Organization, Hours

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

class HoursViewSet(viewsets.ModelViewSet):
    queryset = Hours.objects.all()
    serializer_class = HoursSerializer

class HoursByOrgIdViewSet(generics.ListAPIView):
    serializer_class = HoursSerializer

    def get_queryset(self):
        org_id = self.kwargs['org_id']
        return Hours.objects.filter(organization=org_id)

class HoursByIdViewSet(generics.ListAPIView):
    serializer_class = HoursSerializer

    def get_queryset(self):
        hour_id = self.kwargs['hour_id']
        return Hours.objects.filter(id=hour_id)

class HoursUpdateByIdViewSet(generics.UpdateAPIView):
    serializer_class = HoursSerializer

    def update(self, request, *args, **kwargs):
        hour_id = self.kwargs['hour_id']
        hour = Hours.objects.get(id=hour_id)
        hour.day = hour.day if 'day' not in request.data else request.data['day']
        hour.open_time = hour.open_time if 'open_time' not in request.data else request.data['open_time']
        hour.close_time = hour.close_time if 'close_time' not in request.data else request.data['close_time']
        hour.save()
        return HttpResponse(status=204)


class HoursDeleteByIdViewSet(generics.DestroyAPIView):
    serializer_class = HoursSerializer

    def destroy(self, request, *args, **kwargs):
        hour_id = self.kwargs['hour_id']
        hour = Hours.objects.get(id=hour_id)
        hour.delete()
        return HttpResponse(status=204)

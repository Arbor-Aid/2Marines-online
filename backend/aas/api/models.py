import uuid
from django.db import models

class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField()
    services = models.TextField()
    address = models.CharField(max_length=200)
    county = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    appointment_required = models.BooleanField()
    for_whom = models.TextField()
    def __str__(self):
        return self.name

class Hours(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    day = models.CharField(max_length=10)
    open_time = models.TimeField()
    close_time = models.TimeField()
    def __str__(self):
        return self.organization.name + " " + str(self.day) + " " + str(self.open_time) + "-" + str(self.close_time)

from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    services = models.TextField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    admin_email = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    appointment_required = models.BooleanField()
    restrictions = models.TextField()
    def __str__(self):
        return self.name

class Hours(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    day = models.CharField(max_length=10)
    open_time = models.TimeField()
    close_time = models.TimeField()
    def __str__(self):
        return self.organization.name + " " + str(self.day) + " " + str(self.open_time) + "-" + str(self.close_time)

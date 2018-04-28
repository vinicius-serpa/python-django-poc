from django.db import models

class Profile(models.Model):

    name = models.CharField(max_length = 255, null = False)
    email = models.CharField(max_length = 255, null = False)
    phone = models.CharField(max_length = 15, null = False)
    company_name = models.CharField(max_length = 255, null = False)

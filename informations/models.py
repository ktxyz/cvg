from django.db import models


class InformationMeta(models.Model):
    age = models.PositiveIntegerField()
    name = models.CharField(max_length=256)
    lastname = models.CharField(max_length=256)
    profile_pic = models.ImageField(null=True, blank=True)
    email = models.CharField(max_length=128)
    email_href = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=16)
    interests = models.CharField(max_length=512)

class InformationDetail(models.Model):
    meta = models.ForeignKey(InformationMeta, on_delete=models.CASCADE)
    trans_lang = models.CharField(max_length=5)
    description = models.TextField(max_length=2048)

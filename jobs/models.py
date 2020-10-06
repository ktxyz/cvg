from django.db import models


class JobMeta(models.Model):
    company_name = models.CharField(max_length=256)
    since = models.DateField()
    until = models.DateField()

    def __str__(self):
        return self.company_name

class JobDetail(models.Model):
    job = models.ForeignKey(JobMeta, on_delete=models.CASCADE)
    trans_lang = models.CharField(max_length=5)
    role = models.CharField(max_length=256)
    tech_stack = models.CharField(max_length=256)
    description = models.TextField(max_length=2048)

    def get_tech(self):
        return self.tech_stack.split(',')

    def __str__(self):
        return f"{self.job.company_name}_{self.trans_lang}"
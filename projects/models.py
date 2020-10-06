from django.db import models


class ProjectMeta(models.Model):
    title = models.CharField("title", max_length=256)
    languages = models.CharField("langs", max_length=512, blank=True)
    tools = models.CharField("tools", max_length=512, blank=True)
    homepage = models.CharField(max_length=256, blank=True)
    screen = models.ImageField(null=True, blank=True)

    def get_langs(self):
        return self.languages.split(',')

    def get_tools(self):
        return self.tools.split(',')
    
    def __str__(self):
        return self.title

class ProjectDetail(models.Model):
    project_meta = models.ForeignKey(ProjectMeta, on_delete=models.CASCADE)
    trans_lang = models.CharField(max_length=5)
    keywords = models.CharField("keywords", max_length=512, blank=True)
    description = models.TextField(max_length=2048)

    def get_keywords(self):
        return self.keywords.split(',')

    def __str__(self):
        return f"{self.project_meta.title}_{self.trans_lang}"
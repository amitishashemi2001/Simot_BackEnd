from django.db import models

class SiteInfo(models.Model):
    logo = models.ImageField(upload_to='logo/')
    about_text = models.TextField()
    successful_projects = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "Site Information"


class Slider(models.Model):
    image = models.ImageField(upload_to='slider/')
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title or "Slider Image"


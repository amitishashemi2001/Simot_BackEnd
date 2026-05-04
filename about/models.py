from django.db import models

class AboutCompany(models.Model):
    main_text = models.TextField()  # متن اصلی درباره شرکت
    mission = models.TextField(blank=True)  # ماموریت
    vision = models.TextField(blank=True)   # چشم‌انداز
    values = models.TextField(blank=True)   # ارزش‌ها

    years_experience = models.PositiveIntegerField(default=0)
    employees_count = models.PositiveIntegerField(default=0)
    completed_projects = models.PositiveIntegerField(default=0)
    big_clients = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "About Company"


class CompanyTimeline(models.Model):
    year = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.year} - {self.title}"



class Manager(models.Model):
    name = models.CharField(max_length=150)
    role = models.CharField(max_length=150)  # سمت
    photo = models.ImageField(upload_to='managers/')
    bio = models.TextField(blank=True)
    linkedin = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)

    def __str__(self):
        return self.name




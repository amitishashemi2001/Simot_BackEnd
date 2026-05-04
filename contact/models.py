from django.db import models

class CompanyInfo(models.Model):
    name = models.CharField(max_length=200, verbose_name="Company Name")
    iran_phone = models.IntegerField(verbose_name="Iran Phone Number", null=True)
    uae_phone = models.IntegerField(verbose_name="UAE Phone Number", null=True)
    mobile_phone = models.IntegerField(verbose_name="Mobile Phone Number", null=True)
    email = models.EmailField(verbose_name="Email")
    uae_address = models.TextField(max_length=500, verbose_name="UAE Address", null=True)
    iran_address = models.TextField(max_length=500, verbose_name="Iran Address", null=True)
    social_facebook = models.URLField(blank=True, null=True, verbose_name="Facebook")
    social_instagram = models.URLField(blank=True, verbose_name="Instagram", null=True)
    social_linkedin = models.URLField(blank=True, null=True, verbose_name="LinkedIn")
    hero_image = models.ImageField(upload_to="contact/", blank=True, null=True, verbose_name="Hero Image")

    class Meta:
        verbose_name = "Company Info"
        verbose_name_plural = "Company Info"

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(max_length=200, verbose_name="Subject")
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"{self.name} - {self.subject}"

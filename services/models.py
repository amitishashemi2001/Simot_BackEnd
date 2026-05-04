from django.db import models


class Service(models.Model):
    title_fa = models.CharField(max_length=200, verbose_name="عنوان فارسی")
    title_en = models.CharField(max_length=200, verbose_name="عنوان انگلیسی")

    description_fa = models.TextField(blank=True, null=True, verbose_name="توضیحات فارسی")
    description_en = models.TextField(blank=True, null=True, verbose_name="توضیحات انگلیسی")

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title_fa


class ServiceItem(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name="وابسته به خدمت"
    )

    name_fa = models.CharField(max_length=200, verbose_name="نام فارسی")
    name_en = models.CharField(max_length=200, verbose_name="نام انگلیسی")

    description_fa = models.TextField(blank=True, null=True, verbose_name="توضیحات فارسی")
    description_en = models.TextField(blank=True, null=True, verbose_name="توضیحات انگلیسی")

    image = models.ImageField(upload_to="service_items/", blank=True, null=True, verbose_name="تصویر")

    class Meta:
        verbose_name = "Service Item"
        verbose_name_plural = "Service Items"

    def __str__(self):
        return self.name_fa

from django.db import models

# اختیاری: برای دسته‌بندی (PressRelease, Report, Insight …)
class NewsCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=255)

    summary = models.TextField(
        blank=True,
        help_text="خلاصه برای نمایش در لیست"
    )

    content = models.TextField(
        blank=True,
        help_text="متن کامل خبر"
    )

    image = models.ImageField(
        upload_to='news/images/',
        blank=True,
        null=True
    )

    video = models.FileField(
        upload_to='news/videos/',
        blank=True,
        null=True
    )

    link = models.URLField(
        blank=True,
        null=True,
        help_text="اگر خبر لینک خارجی دارد"
    )

    category = models.ForeignKey(
        NewsCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    published_at = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title

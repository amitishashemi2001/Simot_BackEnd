from django.contrib import admin
from django.utils.html import format_html
from .models import News, NewsCategory

# -----------------------------
# Admin دسته‌بندی‌ها
# -----------------------------
@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


# -----------------------------
# Admin خبرها
# -----------------------------
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'published_at', 'image_tag')
    list_filter = ('category', 'published_at')
    search_fields = ('title', 'summary', 'content')
    readonly_fields = ('image_tag', 'video_tag')

    # -------------------------
    # پیش‌نمایش تصویر در فرم و لیست
    # -------------------------
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height:auto;" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Image'

    # -------------------------
    # پیش‌نمایش ویدیو در فرم جزئیات
    # -------------------------
    def video_tag(self, obj):
        if obj.video:
            return format_html(
                '<video width="200" controls><source src="{}" type="video/mp4"></video>',
                obj.video.url
            )
        return "-"
    video_tag.short_description = 'Video'

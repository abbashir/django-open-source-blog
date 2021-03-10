from django.contrib import admin
from .models import SocialMedia


class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ["name", "icon_class", "url", "status"]
    search_fields = ["title"]
    list_editable = ["status"]

    class Meta:
        model = SocialMedia


# Register your models here.
admin.site.register(SocialMedia, SocialMediaAdmin)

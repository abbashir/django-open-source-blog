from other_pages.models import About, Contact, ContactMessage, GeneralSettings
from django.contrib import admin

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ["title", "email", "phone"]
    list_editable = ["email", "phone"]

    class Meta:
        model = Contact


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "message"]

    class Meta:
        model = ContactMessage


class GeneralSettingsAdmin(admin.ModelAdmin):
    list_display = ["name", "slogan", "footer_text", "base_color"]
    list_editable = ["slogan", "footer_text", "base_color"]

    class Meta:
        model = ContactMessage


admin.site.register(About)
admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(GeneralSettings, GeneralSettingsAdmin)

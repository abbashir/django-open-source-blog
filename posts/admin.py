from django.contrib import admin
from .models import Post, PostCategory


# Register your models here.
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "created_at", "updated_at"]
    list_filter = ["title"]
    search_fields = ["title"]

    prepopulated_fields = {'slug': ('title', )}

    class Meta:
        model = PostCategory


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "author","slug", "feature","view_quantity"]
    list_filter = ["created_at"]
    search_fields = ["title"]
    readonly_fields = ["view_quantity"]
    list_editable = ["feature"]

    # prepopulated_fields = {'slug': ('title', )}


    class Meta:
        model = Post


admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Post, PostAdmin)

from django.contrib import admin

from .models import Post

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "created", "updated")
    prepopulated_fields = {"slug": ("title",)}        #conforme eu preencho  o campo "title", o campo slug vai sendo preenchido também




from django.contrib import admin

from .models import Note, Tag

# Register your models here.


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Note)
admin.site.register(Tag, TagAdmin)

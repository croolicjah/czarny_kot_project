from django.contrib import admin
from posts.models import Post, Section


class PostAdmin(admin.ModelAdmin):
    list_display = ("carousel_title", "order", "section", )
    list_editable = ('section', 'order',)


class SectionAdmin(admin.ModelAdmin):
    list_display = ("name", "order", )
    list_editable = ('order',)


# Register your models here.
admin.site.register(Section, SectionAdmin)
admin.site.register(Post, PostAdmin)




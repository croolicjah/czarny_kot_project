from django.contrib import admin
from django import forms
from django.db import models
from tinymce.widgets import TinyMCE
from posts.models import Post, Section


class PostAdmin(admin.ModelAdmin):
    # edit_date = forms.DateField(label='Data edycji', required=True, widget=forms.TextInput(attrs={'size':'20'}))

    list_display = ("carousel_title", "order", "section", )
    list_editable = ('section', 'order',)

    # fields = [
    #     'edit_date', 'carousel_title', ('photo_carousel_imgur', 'photo_feat_imgur'),
    #     ('feat_title', 'grey_fit_title'), 'lead_carousel_dot', 'lead_feat',
    #     'content', ('section', 'order'), "button_text",
    # ]
    fieldsets = [
        ('Zdjęcia', {
            'fields': (('photo_carousel_imgur', 'photo_feat_imgur'),),
            # 'classes': ('wide', ''),
        }),
        (None, {
            'fields': ('carousel_title', ('feat_title', 'grey_fit_title'), 'lead_carousel_dot', 'lead_feat'),
            'classes': ('wide', ''),
        }),
        (None, {
            'fields': ('content',),
            # 'description': 'Zmiana daty edycji wpłynie na ustawienie posta na stronie',
        }),
        (None, {
            'fields': (('section', 'order'),),
            # 'description': 'Zmiana daty edycji wpłynie na ustawienie posta na stronie',
        }),
        (None, {
            'fields': ('edit_date',),
            # 'description': 'Zmiana daty edycji wpłynie na ustawienie posta na stronie',
        }),
        (None, {
            'fields': ('button_text',),
            'classes': ('collapse',)
            # 'description': 'Zmiana daty edycji wpłynie na ustawienie posta na stronie',
        }),
    ]
    # labels = {
    #     "name": _("Writer"),
    # }
    # description = {
    #     "photo_feat_imgur": "(Proporcja: kwadrat)",
    #     "photo_carousel_imgur": 'proporcja: 1973x1110',
    # }
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


class SectionAdmin(admin.ModelAdmin):
    list_display = ("name", "order", )
    list_editable = ('order',)


# Register your models here.
admin.site.register(Section, SectionAdmin)
admin.site.register(Post, PostAdmin)



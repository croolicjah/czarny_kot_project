from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea

from banners.models import Banner

# admin.site.register(Banner)


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    # edit_date = forms.DateField(label='Data edycji', required=True, widget=forms.TextInput(attrs={'size':'20'}))

    list_display = ('name', 'order', 'link', 'image_banner', 'script')
    list_editable = ('order', 'link', 'image_banner', 'script')

    # fields = [
    #     'edit_date', 'carousel_title', ('photo_carousel_imgur', 'photo_feat_imgur'),
    #     ('feat_title', 'grey_fit_title'), 'lead_carousel_dot', 'lead_feat',
    #     'content', ('section', 'order'), "button_text",
    # ]
    fieldsets = [
        (None, {
            'fields': (('order', 'name'),),
            # 'classes': ('wide', ''),
        }),
        (None, {
            'fields': ('image_banner', 'script'),
            'classes': ('wide', ''),
        }),
        (None, {
            'fields': ('link',),
        }),
    ]

    formfield_overrides = {
        # models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4})},
    }

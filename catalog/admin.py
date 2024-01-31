from django.contrib import admin
from catalog.models import CatalogItem, Author, Publisher


# @admin.register(CatalogItem)
# class CatalogAdmin(admin.ModelAdmin):
#
#
#     fieldsets = [
#         ('Podstawowe', {
#             'fields': ('item_type', 'title', 'sub_title', 'original_title', ('authors', 'translator'), ('series', 'series_number'), ),
#             'classes': ('wide', ''),
#         }),
#         ('Wydanie', {
#             'fields': (
#                 ('publisher', 'edition'), ('first_publication_year', 'publication_year'), 'language', ('kind', 'page_number'),
#                 ('carrier', 'file_format', 'playback_time'), ('ISBN', 'ISSN'),
#             ),
#             'classes': ('wide', ''),
#         }),
        # (None, {
        #     'fields': ('content',),
        #     # 'description': 'Zmiana daty edycji wpłynie na ustawienie posta na stronie',
        # }),
        # (None, {
        #     'fields': (('section', 'order'),),
        #     # 'description': 'Zmiana daty edycji wpłynie na ustawienie posta na stronie',
        # }),
        # (None, {
        #     'fields': (('edit_date', 'state'), ),
        #     # 'description': 'Zmiana daty edycji wpłynie na ustawienie posta na stronie',
        # }),
        # (None, {
        #     'fields': ('button_text',),
        #     'classes': ('collapse',)
        #     # 'description': 'Zmiana daty edycji wpłynie na ustawienie posta na stronie',
        # }),
    # ]


# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Publisher)
# class PublisherAdmin(admin.ModelAdmin):
#     pass

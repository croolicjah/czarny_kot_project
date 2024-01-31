from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    surname = models.CharField(max_length=30, null=True, blank=True)
    nickname = models.CharField(max_length=20, null=True, blank=True)
    summary = models.TextField(null=True, blank=True)


class Publisher(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)



class CatalogItem(models.Model):

    # inventory_number
    # PODSTAWOWE
    item_type = models.CharField(max_length=50, null=True, blank=True, verbose_name='typ pozycji')

    title = models.CharField(max_length=255, blank=True, verbose_name='tytuł')
    sub_title = models.CharField(max_length=255, verbose_name='podtytuł')
    original_title = models.CharField(max_length=255, blank=True, verbose_name='tytuł oryginalny')
    authors = models.ManyToManyField(Author, blank=True, verbose_name='autor')
    translator = models.CharField(max_length=100, blank=True, verbose_name='tłumacz')

    series = models.CharField(max_length=255, blank=True, verbose_name='seria')
    series_number = models.CharField(max_length=30, blank=True, verbose_name='nr w serii')

    # WYDANIE
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, verbose_name='wydawnictwo', null=True, blank=True)
    edition_number = models.CharField(max_length=20, null=True, blank=True, verbose_name='numer wydania')
    # publication_year = models.DateField(null=True, blank=True, verbose_name='data 1. publikacji')
    publication_year = models.DateField(null=True, blank=True, verbose_name='data publikacji')
    language = models.CharField(max_length=20, verbose_name='język', null=True, blank=True)
    edition_place = models.CharField(max_length=255, null=True, blank=True)
    ISBN = models.CharField(max_length=15, blank=True)
    ISSN = models.CharField(max_length=15, blank=True)
    book_form = models.CharField(max_length=15, verbose_name="forma wydania", null=True, blank=True)
    edition_form = models.CharField(max_length=15, verbose_name="forma", null=True, blank=True)
    magazine_number = models.CharField(max_length=20, null=True, blank=True)
    magazine_type = models.CharField(max_length=20, null=True, blank=True)

    dimensions = models.CharField(max_length=40, null=True, blank=True)
    page_number = models.IntegerField(verbose_name='liczba stron')
    # only for electronic editions
    carrier = models.CharField(max_length=20, blank=True, verbose_name='nośnik')
    file_format = models.CharField(max_length=20, blank=True, verbose_name='format pliku')
    playback_time = models.CharField(max_length=10, blank=True, verbose_name='czas odtwarzania')
    notes = models.TextField(null=True, blank=True)

    # KLASYFIKACJA
    # state

    # genre
    # keywords

    # date_collection
    # price =

    # signed
    # gift
    # bought
    # borrowed
    # rating

    # cover
    # summary
    # comments


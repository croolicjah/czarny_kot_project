from operator import itemgetter

from django.core.files.storage import storages
from django.db import models
from django.utils import timezone


STORAGE = storages['imgur']


class Section(models.Model):
    name = models.CharField(max_length=15, verbose_name='Nazwa')
    order = models.IntegerField(default=0, verbose_name='Kolejność')
    image = models.FileField(upload_to='CzornyKotPL', storage=STORAGE, verbose_name='Zdjęcie/ikona sekcji', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sekcja"
        verbose_name_plural = "Sekcje"


class Post(models.Model):
    carousel_title = models.CharField(max_length=45, verbose_name='Tytuł karuzeli i kropki')
    feat_title = models.CharField(max_length=40,  verbose_name='Tytuł fit-a')
    grey_fit_title = models.CharField(
        max_length=40, verbose_name='Szara część tytułu', null=True, blank=True
    )

    photo_carousel = models.ImageField(
        upload_to='img/', verbose_name='Niskie do karuzeli (proporcja 1,78; 1973x1110)', null=True, blank=True
    )
    photo_feat = models.ImageField(upload_to='img/', verbose_name='Zdjęcie fita (kwadrat)', null=True, blank=True)
    photo_carousel_imgur = models.ImageField(
        upload_to='CzornyKotPL', storage=STORAGE, verbose_name='Niskie do karuzeli',
        null=True, blank=True,
        help_text='Proporcja: 1973x1110'
    )
    photo_feat_imgur = models.ImageField(
        upload_to='CzornyKotPL', storage=STORAGE, verbose_name='Do fita i kropki', null=True, blank=True,
        help_text='Proporcja: kwadrat'
    )

    lead_carousel_dot = models.CharField(max_length=100, verbose_name='Lead karuzeli i kropki')
    lead_feat = models.CharField(max_length=255, verbose_name='Lead fit-a', null=True, blank=True)
    content = models.TextField(verbose_name='Treść posta')

    section = models.ForeignKey(
        Section, on_delete=models.PROTECT, verbose_name='Sekcja', related_name="sections", null=True, blank=True
    )
    order = models.IntegerField(verbose_name='Miejsce przypięcia', default=0)

    publication_date = models.DateField(auto_now_add=True, verbose_name='Data publikacji')
    edit_date = models.DateField(default=timezone.now, verbose_name='Data edycji')

    button_text = models.CharField(max_length=25, default='Sprawdź', verbose_name='Napis przycisku')

    def __str__(self):
        return self.carousel_title

    @staticmethod
    def multisort(list_to_sort, specs):
        for key, reverse in reversed(specs):
            list_to_sort.sort(key=itemgetter(key), reverse=reverse)
        return list_to_sort

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posty"



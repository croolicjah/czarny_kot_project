from operator import itemgetter

from django.db import models
from django.utils import timezone


class Section(models.Model):
    name = models.CharField(max_length=15, verbose_name='Nazwa')
    order = models.IntegerField(null=True, blank=True, verbose_name='Kolejność')
    image = models.FileField(upload_to ='sections/', verbose_name='Zdjęcie/ikona sekcji', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sekcja"
        verbose_name_plural = "Sekcje"


class Post(models.Model):
    carousel_title = models.CharField(max_length=45, verbose_name='Tytuł karuzeli i kropki')
    feat_title = models.CharField(max_length=40,  verbose_name='Tytuł fit-a')
    grey_fit_title = models.CharField(
        max_length=40, verbose_name='Szara, 2. część tytułu fit-a', null=True, blank=True
    )
    photo_carousel = models.ImageField(
        upload_to ='img/', verbose_name='Wąskie zdjęcie do karuzeli (proporcja 1,78; 1973x1110)', null=True, blank=True
    )

    photo_feat = models.ImageField(
        upload_to ='img/', default='img/kuszulkiKo_Kwadrat.webp', verbose_name='Zdjęcie do fita (kwadrat)'
    )
    lead_carousel_dot = models.CharField(max_length=100, verbose_name='Lead do karuzeli i kropki')
    lead_feat = models.CharField(max_length=255, verbose_name='Lead do fit-a', null=True, blank=True)
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



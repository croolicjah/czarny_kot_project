from django.db import models
from django.core.files.storage import storages

STORAGE = storages['imgur']


class Banner (models.Model):
    BANNER_TYPE = [
        ('top_banner', 'top-ban'),
        ('inter_banner', 'inter-ban'),
        ('bottom_banner', 'bottom-ban'),
        ('right_banner', 'right-ban'),
        ('sms_banner', 'sms-ban')
    ]

    name = models.CharField(max_length=15, choices=BANNER_TYPE, verbose_name="Typ baneru")
    script = models.TextField( null=True, blank=True, verbose_name="Skrypt/HTML")
    image_banner = models.ImageField(
        upload_to='CzornyKotPL', storage=STORAGE, verbose_name='Obraz',
        null=True, blank=True,
        help_text='format .png, .jpg lub .gif'
    )
    link = models.URLField(max_length=254, verbose_name="Link",  null=True, blank=True)
    order = models.IntegerField(
        default=1, verbose_name="Kolejność",
        help_text="0 - nie pokaże baneru, 1 - dla top, bottom , sms pokaże baner"
    )

    def __str__(self):
        return self.name

    def prepare_banner_set(self):
        __banners = Banner.objects.all().order_by('name', 'order')
        __order_number = 3
        __banner_set = {
            self.BANNER_TYPE[0][0]: None,
            self.BANNER_TYPE[1][0]: {},
            self.BANNER_TYPE[2][0]: None,
            self.BANNER_TYPE[3][0]: {},
            self.BANNER_TYPE[4][0]: None,
        }

        for ban in __banners:
            if ban.name == self.BANNER_TYPE[0][0] and ban.order == 1:
                __banner_set[ban.name] = ban
            elif ban.name == self.BANNER_TYPE[1][0] and ban.order > 0:
                __banner_set[ban.name][__order_number * ban.order] = ban
                # inter_bans needs to have order keys divisible by 3
                # to put them in right place on the site
            elif ban.name == self.BANNER_TYPE[2][0] and ban.order == 1:
                __banner_set[ban.name] = ban
            elif ban.name == self.BANNER_TYPE[3][0] and ban.order > 0:
                __banner_set[ban.name][ban.order] = ban
            elif ban.name == self.BANNER_TYPE[4][0] and ban.order == 1:
                __banner_set[ban.name] = ban
        return __banner_set

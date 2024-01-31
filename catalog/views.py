from django.shortcuts import render
from django.views import View
from catalog.models import CatalogItem
import catalog.catalogs as catalogs


# Create your views here.
class CreateItemView(View):
    def get(self, request):

        context = {
            'book_kind': {bf[0]: bf[1] for bf in sorted(catalogs.BOOK_FORM)},
            'carrier': {bk[0]: bk[1] for bk in sorted(catalogs.CARRIER)},
            'common_forms': {cf[0]: cf[1] for cf in sorted(catalogs.COMMON_FORMS)},
            "cz_catalog": {cc[0]: cc[1] for cc in sorted(catalogs.CZORNY_KOT_CATALOG)},
            "file_formats": {ff[0]: ff[1] for ff in sorted(catalogs.FILE_FORMATS)},
            "magazine_cycle": {mt[0]: mt[1] for mt in sorted(catalogs.MAGAZINE_CYCLE)},
            'types': {t[0]: t[1] for t in sorted(catalogs.ITEM_TYPE)},
        }
        return render(request, 'catalog/detail.html', context=context)

    def post(self, request):
        print('jetem w poscie')
        context = {
            'book_kind': {bf[0]: bf[1] for bf in sorted(catalogs.BOOK_FORM)},
            'carrier': {bk[0]: bk[1] for bk in sorted(catalogs.CARRIER)},
            'common_forms': {cf[0]: cf[1] for cf in sorted(catalogs.COMMON_FORMS)},
            "cz_catalog": {cc[0]: cc[1] for cc in sorted(catalogs.CZORNY_KOT_CATALOG)},
            "file_formats": {ff[0]: ff[1] for ff in sorted(catalogs.FILE_FORMATS)},
            "magazine_cycle": {mt[0]: mt[1] for mt in sorted(catalogs.MAGAZINE_CYCLE)},
            'types': {t[0]: t[1] for t in sorted(catalogs.ITEM_TYPE)},
        }
        return render(request, 'catalog/detail.html', context=context)

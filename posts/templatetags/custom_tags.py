from operator import itemgetter

from django import template
from django.utils.text import slugify
from posts.models import Post, Section

register = template.Library()
register.simple_tag(name="nav_links_fill")


# tag returns pack of links for navbar (made from sections and kontakt)
@register.simple_tag(name="nav_links_fill")
def get_post_section_links(post_section_value=6, name='Kontakt'):
    navbar_menu = []
    lookup_post = Post.objects.get(pk=post_section_value)
    sections = Section.objects.filter(order__lte=99)
    for section in sections:
        new_item = '#sekcja-' + str(section.id) + '/' + slugify(section.name), section.name, section.order
        navbar_menu.append(new_item)
    navbar_menu.sort(key=itemgetter(2))
    new_item = '#post-' + str(lookup_post.id) + '/' + slugify(lookup_post.carousel_title), name
    navbar_menu.append(new_item)
    return navbar_menu
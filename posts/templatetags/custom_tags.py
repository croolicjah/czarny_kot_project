from django import template
from django.utils.text import slugify
from posts.models import Post, Section

register = template.Library()
register.simple_tag(name="get_link")

# tag returns section  link if only value argument added or post if order False (get post by id)
@register.simple_tag(name="get_link")
def get_post_section_link(value, order='True'):
    if order:
        lookup_section = Section.objects.get(order=value)
        return '../#' + slugify(lookup_section.name)  + '-' + str(lookup_section.id)
    else:
        lookup_post = Post.objects.get(pk=value)
        return '../#post-' + str(lookup_post.id) + '/' + slugify(lookup_post.carousel_title)




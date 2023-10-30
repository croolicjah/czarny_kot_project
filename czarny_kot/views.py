from operator import itemgetter

from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import View
from posts.models import Post, Section


class HomeViews(View):
    def get(self, request):

        posts = Post.objects.all()
        sections = Section.objects.all()

        list_of_posts = [
            (section.order, section.name, post, post.edit_date, post.order)
            for section in sections for post in posts if post.section_id == section.id
        ]

        posts_on_site = Post.multisort(list_of_posts, ((0, False), (3, True)))
        carousel_posts = sorted([item for item in posts_on_site if 0 < item[2].order < 4], key=itemgetter(4))
        dot_posts = sorted([item for item in posts_on_site if 3 < item[2].order < 7], key=itemgetter(4))

        context = {
            'carousel_posts': carousel_posts,
            'dot_posts': dot_posts,
            'section_posts': posts_on_site,
        }
        return render(request, 'czarny_kot/front-page.html', context=context)

    def post(self, request):
        return True



# @login_required(login_url="/accounts/signup")
# def create(request):
#     if request.method == 'POST':
#
#     else:
#         return render(request, 'products/create.html')
#
#
# def detail(request, product_id):
#     product = get_object_or_404(Product, pk=product_id)
#     return render(request, 'products/detail.html',{'product':product})
#
#
# @login_required(login_url="/accounts/login")
# def upvote(request, product_id):
#     if request.method == 'POST':
#         product = get_object_or_404(Product, pk=product_id)
#
#         if Product.objects.filter(vote__voter=request.user, vote__product=product).exists():
#             return render(request, 'products/detail.html',{'product':product, 'error': "You have already voted on this product"})
#         else:
#             product.votes_total += 1
#             Vote(product_id=product.id, voter_id=request.user.id).save()
#             product.save()
#             return redirect('/products/' + str(product.id))

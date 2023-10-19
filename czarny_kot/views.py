from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import View

# from .models import Product, Vote
from django.utils import timezone




class HomeViews(View):
    def get(self, request):

        return render(request, 'base.html', {})

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

from django.http import HttpResponse
from django.shortcuts import render

from book.serializer import BookSerializer
from .models import Book
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
def list_product(request):
	context = {'products' : Book.objects.all()}
	return render(request, 'product/product.html', context)
def product_detail(request,slug):
	product=Book.objects.get(slug=slug)
	product_cate=product.Book_Category.all()
	context={'product':product,'p_cate':product_cate}
	return render(request, 'product/product_detail.html', context)
def search_product(request):
	if 'keyword' in request.GET:
		keyword=request.GET.get('keyword')
		products=Book.objects.filter(title__icontains=keyword)
		context={'products':products}
		return render(request, 'product/product.html', context)

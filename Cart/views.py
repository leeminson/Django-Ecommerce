import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *
# Create your views here.
def get_cart(request):
	if request.user.is_authenticated:
		user=request.user
		cart,created=Cart.objects.get_or_create(user=user)
		items=cart.cartitem_set.all()
	else :
		items=[]	
	context = {'items':items,'cart':cart}
	return render(request, 'cart/cart.html', context)
def add_to_cart(request):
	data=json.loads(request.body)
	product_id=data['product_id']
	act=data['act']
	quantity=data['quantity']
	user=request.user
	product=Book.objects.get(id=product_id)
	cart,cart_created=Cart.objects.get_or_create(user=user)
	cartitem,created=CartItem.objects.get_or_create(cart=cart,book_id=product.id)
	print(created)
	if(created is True):
		cartitem.quantity=1
	else:
		cartitem.quantity=(cartitem.quantity+int(quantity))
	cartitem.save()
	return JsonResponse('Added successfully',safe=False)
from django.shortcuts import render

# Create your views here.
def catalog(request):
	context = {}
	return render(request, 'catalog/catalog.html', context)
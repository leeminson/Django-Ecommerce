from django.shortcuts import render
from django.template import RequestContext
from S_A_D import settings
from search import search
from django.core.paginator import Paginator, InvalidPage, EmptyPage

def results(request, template_name="search/results.html"):
 # get current search phrase
 q = request.GET.get('q', '')
 results = search.products(q).get('products')
 search.store(request, q)
 context={'results':results,'q':q}
 # the usual…
 return render(request,template_name,context) 

from django.shortcuts import render
from book.models import Book
from django.db.models import Q 
from search.models import SearchTerm
STRIP_WORDS = ['a','an','and','by','for','from','in','no','not',
 'of','on','or','that','the','to','with'] 
# Create your views here.
def store(request, q):
 # if search term is at least three chars long, store in db
 if len(q) > 2:
    term = SearchTerm()
    term.q = q
    term.save()
def products(search_text):
   words = _prepare_words(search_text)
   results = {}
   results['products'] = []
   # iterate through keywords
   for word in words:
      products = Book.objects.filter(
      Q(name__icontains=word) |
      Q(description__icontains=word) |
      Q(meta_description__icontains=word) |
      Q(meta_keywords__icontains=word))
      results['products'] = products
   return results
def _prepare_words(search_text):
   words = search_text.split()
   for common in STRIP_WORDS:
      if common in words:
         words.remove(common)
   return words[0:5]        
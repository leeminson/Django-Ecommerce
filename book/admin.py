from django.contrib import admin

from book.models import Book,Author,Publisher,BookCategory

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookCategory)

admin.site.register(Publisher)
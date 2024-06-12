from django.db import models
from book.models import Book
from django.contrib.auth.models import User
# Create your models here.
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank = True)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return str(self.id)
    def get_cart_total(self):
        cartitems=self.cartitem_set.all()
        total=sum([item.get_total for item in cartitems])
        return total
    def get_total_item(self):
        cartitems=self.cartitem_set.all()
        total=cartitems.count()
        return total
class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    book_id=models.IntegerField()
    date_added=models.DateField(auto_now_add=True)
    quantity=models.IntegerField(null=True)
    def __str__(self) :
        return self.get_book().name
    @property
    def get_total(self):
        total=(self.get_book().price) *(self.quantity)
        return total
    def get_book(self):
        try:
            book = Book.objects.get(id=self.book_id)
            return book
        except Book.DoesNotExist:
            return None
from django.db import models
from django.utils.text import slugify


# Create your models here.
class BookCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True),
    description = models.TextField(),
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name
class Author(models.Model):
    class gender(models.TextChoices):
        Male='Male'
        Female='Female'
    name=models.CharField(max_length=255,unique="true")
    slug=models.SlugField(max_length=50,unique="true",editable=False)
    gender=models.CharField(max_length=25,
                            choices=gender.choices,
                            default=gender.Male)
    def __str__(self) -> str:
        return self.name 
    def save(self , *args , **kwargs):
        self.slug = slugify(self.name)
        super(Author ,self).save(*args , **kwargs)
        print('slug:'+self.slug) 
class Publisher(models.Model):
    name=models.CharField(max_length=255,unique="true")
    slug=models.SlugField(max_length=50,unique="true",editable=False)
    address=models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name
class Book(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True,editable=False,
    help_text='Unique value for product page URL, created from name.')
    img=models.ImageField(upload_to="img/")
    description = models.TextField()
    price = models.IntegerField()
    is_available = models.BooleanField(default=True)
    meta_keywords = models.CharField("Meta Keywords",max_length=255,help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField("Meta Description", max_length=255,
    help_text='Content for description meta tag') 
    updated_at = models.DateTimeField(auto_now=True)
    publisher=models.ForeignKey(Publisher,on_delete=models.CASCADE)
    numberofpage=models.IntegerField()
    Book_Category=models.ManyToManyField(BookCategory)
    created_at = models.DateTimeField(auto_now_add=True)
    authors=models.ManyToManyField(Author)
    def __str__(self) -> str:
        return self.name 
    def save(self , *args , **kwargs):
        self.slug = slugify(self.name)
        super(Book ,self).save(*args , **kwargs)
        print('slug:'+self.slug)

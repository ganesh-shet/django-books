from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
#Many-to-Many
class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    def countries(self):
        return self.name
    
    def __str__(self):
         return self.countries()

    class Meta:
        verbose_name_plural = "Countries"



#One-to-One
class Address(models.Model):
    street = models.CharField(max_length=80)
    postal = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def address(self):
        return f"{self.street} {self.postal} {self.city}"
    
    def __str__(self):
         return self.address()

    class Meta:
        verbose_name_plural = "Address Entries"

#One-to-One
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
         return self.full_name()

class Book(models.Model):
    title = models.CharField(max_length=50)
    ratings = models.IntegerField(
        validators = [MinValueValidator(1), MaxValueValidator(5)]
        )
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="Books")
    isBestSeller = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank = True, null=False, db_index=True) ##Lord Of the Rings => lord-of-the-rings
    
    published_countries = models.ManyToManyField(Country)


    def get_absolute_urls(self):
        return reverse("book-details", args=[self.slug])

    def __str__(self):
        return f"({self.title}) ({self.ratings})"
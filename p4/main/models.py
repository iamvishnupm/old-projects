from django.db import models
from django.urls import reverse

class Categories(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
    def get_url(self):
        return reverse("c_home", args=self.slug)


class product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    img = models.ImageField(upload_to="products")
    price = models.IntegerField()
    desc = models.TextField()
    stock = models.IntegerField()
    availability = models.BooleanField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
    
    def get_url(self):
        return reverse('details', args=[self.category.slug, self.slug])
    

class Cart(models.Model):
    pd = models.OneToOneField(product,on_delete=models.CASCADE)
    qty = models.IntegerField()
    price = models.IntegerField()
    
    class Meta:
        ordering = ('id',)
        verbose_name = 'Cart'
        verbose_name_plural = 'Cart Items'
    
    def save(self, *args, **kwargs):
        self.price = self.qty * self.pd.price
        return super().save(*args, **kwargs)
    
    def set_price(self):
        self.price = self.qty * self.pd.price

'''
All the product related models
'''
from django.db import models
from django.utils.text import slugify
from .warehouse_models import Warehouse


class Category(models.Model):
    '''
    Details about product category
    '''
    objects = models.Manager()
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200,unique=True,null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super(Category, self).save(*args, **kwargs)

    def generate_unique_slug(self):
        '''
        for generating unique slugs
        '''
        original_slug = slugify(self.name)
        unique_slug = original_slug
        num = 1
        # Check for existing slugs and append a number if necessary
        while Category.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{original_slug}-{num}"
            num += 1
        return unique_slug
    
    def __str__(self):
        return str(self.name)

class Product(models.Model):
    '''
    Contains all the product details
    '''
    objects = models.Manager()
    sku_code = models.CharField(max_length=255, unique=True, primary_key=True) # stock keeping unit
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier_company = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=200,unique=True,null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super(Product, self).save(*args, **kwargs)
    
    def generate_unique_slug(self):
        ''' for unique slug generation '''
        original_slug = slugify(self.name)
        unique_slug = original_slug
        num = 1
        while Product.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{original_slug}-{num}"
            num += 1
        return unique_slug
    
    def __str__(self):
        return str(self.name)
 
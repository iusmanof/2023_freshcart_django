from django.db import models

# Create your models here.
class Category(models.Model):
    title_category = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title_category

class SubCategory(models.Model):
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    title_subcategory = models.CharField(max_length=255, verbose_name="Nom")
    class Meta:
        verbose_name_plural = 'Subcategories'

    def __str__(self):
        return self.title_subcategory


class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory,related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='items_image', blank=True, null=True)
    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
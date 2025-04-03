from django.db import models

class Category(models.Model):
    name = models.CharField( max_length=100 )
    description = models.CharField(max_length=250)
    def __str__(self):
        return self.name
    
class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField( max_length=150)
    description = models.CharField( max_length=250)
    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField( max_digits=12, decimal_places=2)
    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"Image for {self.product.name}"

class Cart(models.Model):
    product = models.ForeignKey(Product, verbose_name=("cart_products"), on_delete=models.CASCADE)
    amount = models.IntegerField()
    def __str__(self):
        return f"Added {self.amunt} {self.product.name}"

class Saved(models.Model):
    product = models.ForeignKey(Product,  verbose_name=('saved_products'), on_delete=models.CASCADE)
    def __str__(self):
        return self.product.name


from django.db import models
class Product(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    slug=models.SlugField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    img=models.ImageField(upload_to='')
    def __str__(self):
        return self.title
class Cart(models.Model):
    cart_id=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.IntegerField()
    timestamp=models.DateTimeField(auto_now=True)
    product= models.ForeignKey(Product,on_delete=models.PROTECT)

    def __str__(self):
        return self.product.title    
    def update_quantity(self,quantity):
        self.quantity+=quantity
        self.save()
    def total(self):
        return self.quantity*self.price
class Buy(models.Model):
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity=models.IntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.product.title+'_'+str(self.id)
             
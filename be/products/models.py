from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products', default='image-not-available.jpg')
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()


    def __str__(self):
        return self.title


class ShoppingCart(models.Model):
    user = models.OneToOneField('users.Patient', on_delete=models.CASCADE, primary_key=True)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"
    
    def get_total(self):
        return self.quantity * self.item.price


class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code


class Order(models.Model):
    user = models.ForeignKey('users.Patient', on_delete=models.CASCADE)
    items = models.ManyToManyField(ShoppingCart)
    ordered = models.BooleanField(default=False)
    created = models.DateField(auto_now=True)
    coupon = models.ManyToManyField(Coupon, blank=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    def get_totals(self):
        total = 0
        for order_item in self.orderitems.all():
            total += order_item.get_total()

        if self.coupon:
            total -+ self.coupon.amount

        return total

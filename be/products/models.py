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


class Order(models.Model):
    user = models.ForeignKey('users.Patient', on_delete=models.CASCADE)
    items = models.ManyToManyField(ShoppingCart)
    ordered = models.BooleanField(default=False)
    created = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    def get_totals(self):
        total = 0
        for order_item in self.orderitems.all():
            total += order_item.get_total()

        return total





# from django.db import models


# class Category(models.Model):
#     title = models.CharField(max_length=100)

#     def __str__(self):
#         return self.title


# class ProductInfo(models.Model):
#     """
#     Holds common information shared by all types of products
#     """
#     title = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='products', default='image-not-available.jpg')
#     description = models.TextField(blank=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     price = models.PositiveIntegerField()

#     class Meta:
#         abstract = True

#     def __str__(self):
#         return self.title


# class Medicines(ProductInfo):
#     pass

# class AyurvedicMedicines(ProductInfo):
#     pass

# class HealthSupplements(ProductInfo):
#     pass

# class DailyEssentials(ProductInfo):
#     pass


# class ShoppingCart(models.Model):
#     user = models.OneToOneField('users.Patient', on_delete=models.CASCADE, primary_key=True)
#     medicines = models.ForeignKey(Medicines, on_delete=models.CASCADE, null=True, blank=True)
#     ayurvedic = models.ForeignKey(AyurvedicMedicines, on_delete=models.CASCADE, null=True, blank=True)
#     supplements = models.ForeignKey(HealthSupplements, on_delete=models.CASCADE, null=True, blank=True)
#     essentials = models.ForeignKey(DailyEssentials, on_delete=models.CASCADE, null=True, blank=True)
#     quantity = models.PositiveIntegerField(default=1)
#     purchased = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.user.first_name + ' ' + self.user.last_name
    
#     def get_total(self):
#         med_total = self.medicines.price * self.quantity
#         ayur_total = self.ayurvedic.price * self.quantity
#         supp_total = self.supplements.price*self.quantity
#         essen_total = self.essentials.price*self.quantity
#         total = med_total+ ayur_total+ supp_total+ essen_total
#         return total


# class Order(models.Model):
#     user = models.ForeignKey('users.Patient', on_delete=models.CASCADE)
#     orderitems = models.ManyToManyField(ShoppingCart)
#     order_placed = models.BooleanField(default=False)
#     created = models.DateField(auto_now=True)

#     def __str__(self):
#         return self.user.first_name + ' ' + self.user.last_name

#     def get_totals(self):
#         total = 0
#         for order_item in self.orderitems.all():
#             total += order_item.get_total()

#         return total
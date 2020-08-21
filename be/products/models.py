from django.db import models


class ProductInfo(models.Model):
    """
    Holds common information shared by all types of products
    """
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products', default='image-not-available.jpg')
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Medicines(ProductInfo):
    def __str__(self):
        return self.title

class AyurvedicMedicines(ProductInfo):
    def __str__(self):
        return self.title

class HealthSupplements(ProductInfo):
    def __str__(self):
        return self.title

class DailyEssentials(ProductInfo):
    def __str__(self):
        return self.title

class Category(models.Model):
    medicines = models.ForeignKey(Medicines, on_delete=models.CASCADE)
    ayurvedic = models.ForeignKey(AyurvedicMedicines, on_delete=models.CASCADE)
    supplements = models.ForeignKey(HealthSupplements, on_delete=models.CASCADE)
    essentials = models.ForeignKey(DailyEssentials, on_delete=models.CASCADE)


class ShoppingCart(models.Model):
    user = models.OneToOneField('users.Patient', on_delete=models.CASCADE, primary_key=True)
    items = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now=True)

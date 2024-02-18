from django.db import models

# Create your models here.
 

class category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.name 


class product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    image = models.ImageField(null=True)
    price = models.FloatField(null=True)
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.product_name



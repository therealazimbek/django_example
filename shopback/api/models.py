from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150) 

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(default=10.99)
    description = models.TextField(blank=True, null=True)
    count = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'is_active': self.is_active,
            'category': self.category.name  
        }    

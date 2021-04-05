from django.db import models

class Meal(models.Model):
    portions = (
        ('0.7', '0.7'),
        ('1', '1')
    )
    image = models.ImageField(blank=True, null=True, verbose_name='Изображение')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=0)
    portion = models.CharField(choices=portions, max_length=50)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

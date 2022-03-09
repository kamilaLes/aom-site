from enum import unique
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Trainer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to = "images")
    content = models.TextField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

class Equipment(models.Model):
    class Meta:
        verbose_name_plural = "Equipment"
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Classes(models.Model):
    class Meta:
        verbose_name_plural = "Classes"
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=300)
    image = models.ImageField(upload_to = "images")
    content = models.TextField()
    slug = models.SlugField(unique=True, db_index=True)
    trainer = models.ManyToManyField(Trainer)
    equipment = models.ManyToManyField(Equipment)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    phone = PhoneNumberField(unique=True, null=True)
    classes = models.ManyToManyField(Classes)

    def __str__(self):
        return self.first_name + " " + self.last_name

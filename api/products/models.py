from django.db import models
from django.core.validators import RegexValidator, MinValueValidator

alphanumeric_validator = RegexValidator(
    regex=r'^[0-9A-Za-z]{6,10}$',
    message="Part Number must be 6 to 10 alphanumeric characters."
)

class Product(models.Model):
    name = models.CharField(max_length=100)
    colour = models.CharField(max_length=50)
    part_number = models.CharField(
        max_length=10, 
        unique=True,
        validators=[alphanumeric_validator]
    )
    size_mm = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.part_number})"

from django.db import models
from users.models import CustomUser

class Item(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, default='on-sale')
    owner = models.ForeignKey(CustomUser, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

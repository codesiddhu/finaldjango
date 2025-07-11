from django.db import models

# Create your models here.
class Admission(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    address = models.TextField()
    def __str__(self):
        return  f"{self.name} - {self.email} - {self.phone} - {self.date_of_birth} - {self.address}"
    class Meta:
        verbose_name = "Admission"
        verbose_name_plural = "Admissions"
        

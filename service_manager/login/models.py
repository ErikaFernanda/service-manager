from django.db import models
from home.models import Company
# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin , AbstractUser



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O campo de e-mail deve ser definido')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.company_id=1
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)
    
class User(AbstractUser):
    name = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='users')
    
    objects = CustomUserManager()

    def __str__(self):
        return self.name
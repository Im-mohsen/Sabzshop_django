from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
# Create your models here.


class ShopUserManager(BaseUserManager):
    def create_user(self,phone, password=None, **extra_fields):
        if not phone:
            raise ValueError('You must provide a phone!')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff must be True!')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser must be True!')

        return self.create_user(phone, password, **extra_fields)


class ShopUser(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=11, unique=True, verbose_name='شماره تلفن')
    first_name = models.CharField(max_length=25, verbose_name='نام')
    last_name = models.CharField(max_length=25, verbose_name='نام خانوادگی')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = ShopUserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.phone}"


class Address(models.Model):
    user = models.ForeignKey(ShopUser, related_name='addresses', on_delete=models.CASCADE)
    address = models.TextField(max_length=250, verbose_name='آدرس')
    is_default = models.BooleanField(default=False, verbose_name='آدرس پیش فرض')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    postal_code = models.CharField(max_length=10, verbose_name='کدپستی')
    province = models.CharField(max_length=50, verbose_name='استان')
    city = models.CharField(max_length=50, verbose_name='شهر')

    class Meta:
        ordering = ['is_default', '-created']
        indexes = [
            models.Index(fields=['-created'])
        ]
        verbose_name = "آدرس"
        verbose_name_plural = "آدرس ها"

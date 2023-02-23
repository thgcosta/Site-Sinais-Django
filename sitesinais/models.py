from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, whatsapp_number=None, referal=None):
        if not email:
            raise ValueError('Insira um email!')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            whatsapp_number=whatsapp_number,
            referal=referal
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None, whatsapp_number=None, referal=None):
        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            whatsapp_number=whatsapp_number,
            referal=referal
        )

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    whatsapp_number = models.CharField(max_length=20, blank=True, null=True)
    referal = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_trusty = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

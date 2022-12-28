from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser


class MyUserManager(BaseUserManager):
    """
    Django requires that custom users define their own Manager class. By
    inheriting from `BaseUserManager`, we get a lot of the same code used by
    Django to create a `User`.

    All we have to do is override the `create_user` function which we will use
    to create `User` objects.
    """

    def _create_user(self, email, first_name, last_name, password=None, **extra_fields):
        if not first_name:
            raise ValueError('The given first_name must be set')

        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name=last_name, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        """
        Create and return a `User` with an email and password.
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, first_name, last_name, password, **extra_fields)

    def create_superuser(self, email, first_name, last_name, password, **extra_fields):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, first_name, last_name, password, **extra_fields)


# Create your models here.
class MyUser(AbstractBaseUser, PermissionsMixin):  
    email = models.EmailField(('Email Address'), unique=True, max_length=255)
    first_name = models.CharField(('First Name'), db_index=True, max_length=255)
    last_name = models.CharField(('Last Name'), db_index=True, max_length=255, null=True)
    is_active = models.BooleanField(('is active?'), default=True)
    is_staff = models.BooleanField(('is staff?'), default=False)

    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    REQUIRED_FIELDS = ('first_name', 'last_name', )

    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.email}"


    def get_full_name(self):
        """
        This method is required by Django for things like handling emails.
        Typically this would be the user's first and last name. Since we do
        not store the user's real name, we return their username instead.
        """
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        """
        This method is required by Django for things like handling emails.
        Typically, this would be the user's first name. Since we do not store
        the user's real name, we return their username instead.
        """
        return self.first_name     


    def get_username(self):
        return self.email



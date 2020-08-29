from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, username, password, name):
        user = self.model(
            username=username,
            password=password,
            name=name
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, name):

        user = self.create_user(
            username=username,
            password=password,
            name=name
        )
        user.is_admin = True
        user.save()
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    name     = models.CharField(max_length=200)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'name']

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


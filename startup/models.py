from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


from .managers import CustomUserManager

class Profession(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class CustomUser(AbstractBaseUser, PermissionsMixin):
    #is_staff = models.BooleanField(default=False)
    #is_active = models.BooleanField(default=True)
    #date_joined = models.DateTimeField(default=timezone.now)


    name = models.CharField(max_length=200, unique=True, verbose_name=u"Логин")
    email = models.EmailField(_("email address"), null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)


    full_name = models.CharField(max_length=200, verbose_name=u"ФИО")
    profession = models.ForeignKey(Profession, null=True, blank=True, on_delete=models.SET_NULL, verbose_name=u"ДОЛЖНОСТЬ")
    fired = models.BooleanField(default=False, verbose_name=u"Уволен")
    fired_date = models.DateTimeField(blank=True, null=True, verbose_name=u"Дата Увольнения")


    USERNAME_FIELD = "name"
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    #def __str__(self):
    #    return self.email

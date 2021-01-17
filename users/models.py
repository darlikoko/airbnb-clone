from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "Other"
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_MYANMAR = "my"
    LANGUAGE_JAPAN = "jp"
    LANGUAGE_CHOICES = ((LANGUAGE_MYANMAR, "Myanmar"), (LANGUAGE_JAPAN, "Japan"))

    CURRENCY_MYANMAR = "KYT"
    CURRENCY_JAPAN = "YEN"
    CURRENCY_CHOICES = ((CURRENCY_MYANMAR, "Kyat"), (CURRENCY_JAPAN, "Yen"))

    avator = models.ImageField(blank=True)
    bio = models.TextField(blank=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)
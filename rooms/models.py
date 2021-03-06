from django.db import models
from core import models as core_models
from django_countries.fields import CountryField


class AbstarctItem(core_models.TimeStampedModel):
    """Abstract Items"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstarctItem):
    class Meta:
        verbose_name = "Room Type"


class Amenity(AbstarctItem):
    class Meta:
        verbose_name_plural = "Amenties"


class Facility(AbstarctItem):
    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstarctItem):
    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):
    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)


class Room(core_models.TimeStampedModel):
    """Room Model Definations"""

    name = models.CharField(max_length=140)
    descriprion = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room_type = models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField("Amenity", blank=True)
    facilities = models.ManyToManyField("Facility", blank=True)
    house_rules = models.ManyToManyField("HouseRule", blank=True)

    def __str__(self):
        return self.name

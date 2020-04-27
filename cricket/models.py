from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
import uuid


class Kheladi(models.Model):
    ROLE_CHOICES =(
        ('all rounder', 'all rounder'),
        ('bowler', 'bowler'),
        ('batsman', 'batsman'),
    )
    BATTING_CHOICES = (
        ('right hand bat', 'right hand bat'),
        ('left hand bat', 'left hand bat'),
    )
    BOWLING_CHOICES = (
        ('right arm fast', 'right arm fast'),
        ('left arm fast', 'left arm fast'),
        ('left arm spin', 'left arm spin'),
        ('right arm spin', 'right arm spin'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField()
    favourite_cricketer = models.CharField(max_length=30)
    dp = models.ImageField(upload_to='profile/', blank=True, null=True)
    country = models.CharField(max_length=7)
    slug = models.SlugField(blank=True, null=True, editable=False)
    uuid = models.UUIDField(blank=True, null=True, default=uuid.uuid4)
    dob = models.DateField(default=timezone.now, help_text='Enter in format YYYY-MM-DD')
    age = models.PositiveIntegerField(blank=True)
    height = models.CharField(default=0, max_length=10)
    role = models.CharField(choices=ROLE_CHOICES, max_length=20, default='all rounder')
    contact = models.CharField(max_length=30, blank=True, null=True)
    batting_style = models.CharField(choices=BATTING_CHOICES, max_length=20, default='right hand bat')
    bowling_style = models.CharField(choices=BOWLING_CHOICES, max_length=20, default='right arm bowl')
    highest_score = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(200)])
    highest_wicket = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])

    def __str__(self):
        return self.first_name

    def save(self, **kwargs):
        print()
        if not self.age:
            self.age = int((timezone.now().date() - self.dob).days / 365)
        if not self.slug:
            self.slug = slugify(f'{self.first_name} {self.last_name}')
        super(Kheladi, self).save(**kwargs)


    def get_absolute_url(self):
        return reverse('cricket:player_detail', kwargs={'slug': self.slug, 'uuid': self.uuid})

    class Meta:
        verbose_name_plural = 'Kheladi'
        ordering = ['first_name']

# class Match(models.Model):
#     odi_played =
#     test_played =
#     t20_played =



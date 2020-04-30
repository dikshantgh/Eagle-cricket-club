from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
import uuid
from cloudinary.models import CloudinaryField


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
    first_name = models.CharField(max_length=50, db_index=True)
    last_name = models.CharField(max_length=50, )
    bio = models.TextField(db_index=True)
    favourite_cricketer = models.CharField(max_length=30, db_index=True)
    dp = CloudinaryField(verbose_name='profile picture', db_index=True)
    country = models.CharField(max_length=7, db_index=True)
    slug = models.SlugField(blank=True, null=True, editable=False, db_index=True)
    uuid = models.UUIDField(blank=True, null=True, default=uuid.uuid4, db_index=True)
    dob = models.DateField(verbose_name='Date of Birth', default=timezone.now, help_text='Enter in format YYYY-MM-DD', db_index=True)
    age = models.PositiveIntegerField(blank=True, db_index=True)
    height = models.CharField(default=0, max_length=10, db_index=True)
    role = models.CharField(choices=ROLE_CHOICES, max_length=20, default='all rounder', db_index=True)
    contact = models.CharField(max_length=30, blank=True, null=True, db_index=True)
    batting_style = models.CharField(choices=BATTING_CHOICES, max_length=20, default='right hand bat', db_index=True)
    bowling_style = models.CharField(choices=BOWLING_CHOICES, max_length=20, default='right arm bowl', db_index=True)
    highest_score = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(200)], db_index=True)
    highest_wicket = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)], db_index=True)

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


class Gang(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_index=True)
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    in_mind = models.TextField(verbose_name='Whats in your mind?', db_index=True)

    def __str__(self):
        return self.author.username

    def get_absolute_url(self):
        return reverse('cricket:gang_share')


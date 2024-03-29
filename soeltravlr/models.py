from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from datetime import date, datetime

SEASONS = (
    ('Summer', 'Summer'),
    ('Spring', 'Spring'),
    ('Fall', 'Fall'),
    ('Winter', 'Winter')
    )


# Create your models here.
class Travel(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(
        User, on_delete = models.CASCADE)
    body = models.TextField()
    rating = models.IntegerField(
        default=1, validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    season = models.CharField(choices=SEASONS)
    travel_date = models.CharField()
    image = models.ImageField(upload_to="static/images/", null=False, blank=False, default="")
    review_date = models.DateField()
    like = models.ManyToManyField(User, related_name = 'blog_travel')

    def likes(self):
        return self.like.count()

    class Meta:
        ordering = ["-travel_date"]

    def __str__(self):
        return self.title + ', by ' + str(self.author)

    def __get_absolute_url(self):
        return reverse('post-detail', args(str(self.id)))

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    bio = models.TextField(max_length=1000, default="")
    pic = models.ImageField(upload_to="static/images/", null=True, blank=True, default="")
    social_media = models.CharField(max_length=500, null=True, blank=True)
    website = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.user)

class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete = models.CASCADE)
    body = models.CharField(max_length=500)
    travel = models.ForeignKey(
        Travel, on_delete=models.CASCADE, related_name="travel_comments"
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment {self.body}  by {self.author}"
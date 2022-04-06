from tkinter.messagebox import NO
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)
    body = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
#null=Ture, blank=True

    class Meta:
        ordering = ['-created_on']

    def get_absolute_url(self):
        # return f'/post_details/{self.slug}/'
        return reverse("post_details", kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
       # if self.slug is None:
        #    self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title + ' | ' + str(self.author)


def post_pre_save(sender, instance, *args, **kwargs):
    print('pre_save')

    if instance.slug is None:
        instance.slug = slugify(instance.title)


pre_save.connect(post_pre_save, sender=Post)
# class Category(models.Model):
#    name = models.CharField(max_length=)


def post_post_save(sender, instance, created, *args, **kwargs):
    print('post_save')

    if created:
        instance.slug = slugify(instance.title)
        instance.save()


post_save.connect(post_post_save, sender=Post)

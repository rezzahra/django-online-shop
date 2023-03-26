from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    img = models.ImageField(verbose_name=_('product image'), upload_to='product/product_cover/', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detial', args=[self.pk])


class ActiveCommentManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentManager, self).get_queryset().filter(active=True)

class Comment(models.Model):
    CHOICE_STAR = [
        ('1', _('very bad')),
        ('2', _('bad')),
        ('3', _('normal')),
        ('4', _('good')),
        ('5', _('perfect'))
    ]
    auther = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField(verbose_name=_('comment text'))
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    stars = models.CharField(max_length=10, choices=CHOICE_STAR, verbose_name=_('what is your corse?'))
    active = models.BooleanField(default=True)

    #manager
    objects = models.Manager()
    active_comments = ActiveCommentManager()

    def get_absolute_url(self):
        return reverse('detial', args=[self.product.id])
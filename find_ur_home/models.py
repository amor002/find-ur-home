# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse


class set(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

    phone_number = models.IntegerField()

    image = models.FileField(upload_to="users_images/", default='user_img.png')

    def get_absolute_url(self):

        return '/add-user-set/'+str(self.id)

    def __str__(self):
        return str(self.user)


class house(models.Model):
    pub_date = models.DateTimeField("date published", auto_now=True)

    address = models.CharField(max_length=500)

    price = models.IntegerField()

    detail = models.TextField()

    area = models.CharField(max_length=50)

    sold = models.BooleanField(default=False)

    for_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    models

    def __str__(self):

        return self.address

    def get_absolute_url(self):
        return 'add-house/'+str(self.id)


class house_image(models.Model):
    image = models.FileField(upload_to="houses_images/")

    for_house = models.ForeignKey(house, on_delete=models.CASCADE)

    def __str__(self):

        return str(self.image)

    def get_absolute_url(self):
        return '/home/house-select'


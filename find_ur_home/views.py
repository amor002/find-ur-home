# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.utils import timezone
from .models import *
from django.views import generic
from . import forms
from django.contrib.auth.views import login_required
from django.contrib.auth.decorators import permission_required, user_passes_test


class signup(generic.ListView):

    def get(self, request):

        form = forms.signup()

        return render(request, 'find_ur_home/signup_form.html', {'form': form})

    def post(self, request):

        form = forms.signup(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return HttpResponseRedirect(reverse('add-notifications'))

        else:
            return render(request, 'find_ur_home/signup_form.html', {'form': form, 'msg': 'check your inputs or may be this user name have been chosen'})


@login_required(login_url='sign up')
def add_user_set(request, id):

    inf = get_object_or_404(set, pk=int(id))

    inf.user = request.user

    inf.save()

    return HttpResponseRedirect(reverse('home'))



class add_notifications(generic.CreateView):

    model = set

    template_name = 'find_ur_home/signup_form.html'

    fields = ['phone_number', 'image']


def if_login(request):

    if request.user.is_anonymous:

        return HttpResponseRedirect(reverse('index'))

    else:
        return HttpResponseRedirect(reverse('home'))


#-----------------------------------------------------------------------------------------------
@login_required(login_url='index')
def home(request):

    try:
      request.user.set.id
    except:
      return HttpResponseRedirect(reverse('add-notifications'))

    for i in house.objects.all():
        if i.sold:
            i.delete()

    user = request.user

    imaged_house = []
    offered_houses = house.objects.order_by('-pub_date')[:3]

    for HOUSE in house.objects.all():
        if len(HOUSE.house_image_set.all()) != 0:
            imaged_house.append(HOUSE)

    return render(request, "find_ur_home/home.html", {"user": user,
                                                      "houses": offered_houses,
                                                      "imaged_house": imaged_house})

#----------------------------------------------------------------------------------------------

class edit_info(generic.DetailView):

    model = User

    def get(self, request):

        form = forms.edit_info(instance=request.user)

        return render(request, 'find_ur_home/editinfo_form.html', {'form': form, 'user': request.user})

    def post(self, request):

        form = forms.edit_info(request.POST, instance=request.user)

        if form.is_valid():

            form.save()

            return HttpResponseRedirect(reverse('edit-info-2', kwargs={'pk':request.user.set.id}))

        else:
            return render(request, 'find_ur_home/editinfo_form.html', {'form': form, 'user': request.user, 'msg': 'check your inputs or may be this user name have been chosen'})



class edit_info_2(generic.edit.UpdateView):

    model = set

    template_name = 'find_ur_home/editinfo_form.html'

    fields = ['phone_number', 'image']

    success_url = '/home/'

class select_house(generic.ListView):

    model = house_image

    template_name = 'find_ur_home/house_select.html'

    def get(self, request, *args, **kwargs):

        user_products = request.user.house_set.all()

        user = request.user

        imaged_houses = []

        for house in user_products:

            if len(house.house_image_set.all()) != 0:

                imaged_houses.append(house)


        return render(request, self.template_name, {'houses': user_products,
                                                    'user': user,
                                                    'imaged_house': imaged_houses})

class add_house_image(generic.DetailView):

    model = house_image

    def get(self, request, *args, **kwargs):
        form = forms.add_house_image()
        return render(request, 'find_ur_home/about_house.html', {'user': request.user, 'form': form})

    def post(self, request, pk):

        form = forms.add_house_image(request.FILES)
        product = get_object_or_404(house, pk=pk)
        new_image = house_image(image=request.FILES['image'], for_house=product)
        new_image.save()
        return HttpResponseRedirect(reverse('house-select'))

    



class verify_house(generic.CreateView):

    model = house

    template_name = 'find_ur_home/sell_house.html'

    fields = ['address', 'price', 'area', 'detail']


def add_house(request, id):

   this_house = get_object_or_404(house, pk=int(id))

   this_house.for_user = request.user

   this_house.save()

   return HttpResponseRedirect(reverse('home'))


class edit_house(generic.edit.UpdateView):

    model = house

    template_name = 'find_ur_home/edithouse_form.html'

    fields = ['address', 'price', 'area', 'sold', 'detail']

    success_url = '/home/'

def log_out(request):

    logout(request)

    return HttpResponseRedirect(reverse('index'))



class edit_image(generic.ListView):

    model = house_image

    template_name = 'find_ur_home/edithouseimage.html'

    def get(self, request, pk):

        current_house = get_object_or_404(house, pk=pk)

        images_list = current_house.house_image_set.all()

        return render(request, self.template_name, {'user': request.user,
                                                    'house': current_house})



class edit_image2(generic.edit.UpdateView):

    model = house_image

    template_name = 'find_ur_home/edit_house_image.html'

    fields = ['image']

    success_url = '/home/house-select'



class delete_image(generic.edit.DeleteView):

    model = house_image

    template_name = 'find_ur_home/delete_image.html'

    success_url = '/home/house-select'


class search(generic.ListView):

    model = house

    def post(self, request):

        search = request.POST['search']

        suggested_houses = []
        imaged_houses = []

        for i in house.objects.all():

            if search in i.address:

                suggested_houses.append(i)

        for HOUSE in house.objects.all():
            if len(HOUSE.house_image_set.all()) != 0:
               imaged_houses.append(HOUSE)

        if len(suggested_houses) == 0:
            
            return  render(request, 'find_ur_home/home.html', {'user': request.user,
                                                          'houses': suggested_houses,
                                                           'no_result': 'address not found',
                                                           'imaged_houses': imaged_houses})     


        return render(request, 'find_ur_home/home.html', {'user': request.user,
                                                          'houses': suggested_houses,
                                                           'imaged_house': imaged_houses})




    







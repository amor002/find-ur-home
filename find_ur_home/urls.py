from django.conf.urls import url
from . import views
from django.contrib.auth.views import login
from string import letters as l
from random import randint
from django.contrib.auth.views import (password_reset,
                                       password_reset_confirm,
                                       password_reset_done,
                                       password_reset_complete)

letters = ' '.join(l).split(' ')

arry = ''
for i in range(randint(0, len(letters)-1)):

    arry += letters[i]

KEY1 = arry.join(str(randint(0, 100000000)))
KEY2 = arry.join(str(randint(0, 10000000)))


urlpatterns =[

    url(r'^login$', login, {'template_name': 'find_ur_home/index.html'}, name='index'),
    url(r'^log-out$', views.log_out, name='log-out'),
    url(r'^home/house-select$', views.select_house.as_view(), name='house-select'),
    url(r'^home/add-house-image/ 1a2g3g4da1%s(?P<pk>[0-9]+)%s633t3d 21$'%(KEY1, KEY2), views.add_house_image.as_view(), name='add-house-image'),
    url(r'^$', views.if_login),
    url(r'^home/edit-house/ 1f ads2 dfdg 3g1da1%s(?P<pk>[0-9]+)%sTs ft2 d 21$'%(KEY1, KEY2),views.edit_house.as_view(), name='edit-house'),
    url(r'^home/password-reset', password_reset, name='password_reset'),
    url(r'home/passowrd-reset/done', password_reset_done, name='password_reset_done'),
    url(r'home/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'home/done', password_reset_complete, name='password_reset_complete'),
    url(r'^sign up$', views.signup.as_view(), name='sign up'),
    url(r'^home/edit-image/ 1fad131 a1d112s2 df312d2g 3g1d123a1%s(?P<pk>[0-9]+)%sTcx21n21v41342cx fds d 21$'%(KEY1, KEY2),views.edit_image.as_view(), name='edit-image-1'),
    url(r'^home/edit-image-2/ ak123d dk123sf4225mla na123flv2134nxx 13132 123%s(?P<pk>[0-9]+)%sT123cx21123n21v413421423cx 2fds d413 21$'%(KEY1, KEY2),views.edit_image2.as_view(), name='edit-image-2'),
    url(r'^add-notifications$', views.add_notifications.as_view(), name='add-notifications'),
    url(r'^add-user-set/(?P<id>[0-9]+)$', views.add_user_set, name='add-user-set'),
    url(r'^home/$', views.home, name="home"),
    url(r'^home/add-house/(?P<id>[0-9]+)$', views.add_house),
    url(r'^home/edit-info$', views.edit_info.as_view(), name="edit-info"),
    url(r'^home/edit-info-2/ 1a2g3g4da1%s(?P<pk>[0-9]+)%s633t3d 21$'%(KEY1, KEY2), views.edit_info_2.as_view(), name="edit-info-2"),
    url(r'^home/delete-image/ 123123 vdada121%s(?P<pk>[0-9]+)%sad6fa3a3t3d 21$'%(KEY1, KEY2), views.delete_image.as_view(), name="delete-image"),
    url(r'^home/sell-house$', views.verify_house.as_view(), name="verify product"),
    url(r'^home/search$', views.search.as_view(), name='search')


]


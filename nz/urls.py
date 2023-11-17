from nz.views import *

from django.urls import path

app_name='mama'

urlpatterns=[
    path('williamson/',williamson,name='williamson'),
    path('mitchell/',mitchell,name='mitchell'),
]
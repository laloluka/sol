from django.urls import path
from django.conf.urls import include, url
from material.frontend import urls as frontend_urls
from . import views
from django.views import generic
from material.frontend import urls as frontend_urls

from django.shortcuts import render, redirect
urlpatterns=[


    path('',views.home, name='home'),
    # path('edit/<str:pk>/',views.edit, name='edit'),
    # path("edit/", views.edit, name="edit"),
    # url(r'', include(frontend_urls)),
    url(r'^workflow/', generic.RedirectView.as_view(url='/workflow/', permanent=False)),

    # path('update_order/<str:pk>/', views.update_order, name="update_order"),
    path('members/<int:pk>/',views.members, name="members"),
    path('update/<str:pk>/',views.update, name="update"),
    path('export/',views.export, name="export"),

    path('loan/',views.loan, name='loan'),
    path('deposit/',views.deposit, name='deposit'),

#     path('customer/<str:pk_test>/', views.customer, name="customer"),
]
# -*- coding: utf-8 -*-
#######################
# main.urls
#######################
from django.urls import path
from main import views

urlpatterns = [
    path('health/', views.health,name="health"),
    path('query/', views.get_query_json,name="getQueryJson"),
]

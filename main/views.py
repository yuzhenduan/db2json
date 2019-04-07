# -*- coding: utf-8 -*-
#######################
# main.views
#######################
from django.http import HttpResponse
from main.schedule import get_query_result


# health
def health(request):
    return HttpResponse("<h1>Yes, We Can!</h1>")


# /
def get_query_json(request):    
    results=get_query_result(request)
    return HttpResponse(results) 

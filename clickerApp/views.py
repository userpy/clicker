from django.shortcuts import render
from .methods import  LinkCreator, LinkControl
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser, FormParser
from .models import Links
import random
import json
import requests
# Create your views here.
from django.shortcuts import redirect
import re

def index(request, link= None):
    """
    Главная страница
    """
    links = Links.objects.filter(code=link)
    if len(links) > 0:
        return redirect(to=links[0].url)
    else:
        return render(request, 'index.html')




class Link(APIView):
    """
    Генератор ссылок
    """
    parser_classes = (JSONParser, FormParser)
    def post(self, request, format=None):
        url = request.POST.get('link')
        #проверяем работоспособность ссылки
        link_bool = LinkControl(link=url)
        if link_bool:
            #хорошая ссылка
            link = LinkCreator(width=7,
                               url=url,
                               model=Links,
                               template='http://127.0.0.1:8000/')
            response = link.data()
        else:
            #плохая ссылка
            response = 'Некроктные данные'
        return Response(dict(link=response), status=status.HTTP_200_OK)


from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests, json
from mFoods.models import Foods

def index(request):
    query = request.GET.get('q')
    state_temp = ''
    state_weather = ''
    andress = ''
    url =  'http://api.openweathermap.org/data/2.5/weather?q=' + str(query) + '&appid=bd728a9a17c3ccd531c838b88853cc92&units=metric&lang=vi'
    try:
        r = requests.get(url=url)
        data = json.loads(r.text)
        if(data['cod']=='404'):
            pass
        else:
            state_temp =  data['main']['temp']
            state_weather =  data['weather'][0]['description']
            andress =   data['name']
    except:
        pass
    template = loader.get_template('index.html')
    context = {
        'query': query,
        'state_temp': state_temp,
        'state_weather': state_weather, 
        'andress': andress,
    }
    return HttpResponse(template.render(context, request))

def content(request):
    latest_foods_list = Foods.objects.order_by('?')[:50:-1]
    template = loader.get_template('content.html')
    context = {
        'latest_foods_list': latest_foods_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, food_id):
    new_foods_list = Foods.objects.order_by('-create_date')[:5]
    filter_foods_list = Foods.objects.filter(id=food_id)
    template = loader.get_template('detail.html')
    context = {
        'filter_foods_list': filter_foods_list,
        'new_foods_list': new_foods_list,
    }
    return HttpResponse(template.render(context, request))


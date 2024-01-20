from django.shortcuts import render

# Create your views here.
from app.models import *
from app.forms import *
from django.http import HttpResponse


def insert_topic(request):
    ETFO=TopicForms(request.POST)
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForms(request.POST)
        if TFDO.is_valid():
            tn=TFDO.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
            return HttpResponse('Topic is inserted')
        else:
            return HttpResponse('invalid')

    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EWFO=WebPageForms()
    d1={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebPageForms(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topic_name'] 
            TO=Topic.objects.get(topic_name=tn)
            n=WFDO.cleaned_data['name']
            u=WFDO.cleaned_data['url']
            e=WFDO.cleaned_data['email']
            WO=WebPage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
            WO.save()
            return HttpResponse('Web page is created')
        else:
            return HttpResponse('invalid')
        
    return render(request,'insert_webpage.html',d1)

def insert_Accessrecord(request):
    EAFO=AccessRecordForms()
    d2={'EAFO':EAFO}
    if request.method=='POST':
        AFDO=AccessRecordForms(request.POST)
        if AFDO.is_valid():
            na=AFDO.cleaned_data['name']
            WO=WebPage.objects.get(name=na)
            a=AFDO.cleaned_data['author']
            d=AFDO.cleaned_data['date']
            AO=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)[0]
            AO.save()
            return HttpResponse('Access is created')
        else:
            return HttpResponse('Invalid')
        
    return render(request,'insert_Accessrecord.html',d2)
from django import forms
from app.models import *

class TopicForms(forms.Form):
    topic_name=forms.CharField()


class WebPageForms(forms.Form):
    tl=([to.topic_name,to.topic_name] for to in Topic.objects.all())
    topic_name=forms.ChoiceField(choices=tl)
    name=forms.CharField()
    url=forms.URLField()
    email=forms.EmailField()

class AccessRecordForms(forms.Form):
    nl=([no.pk,no.name] for no in WebPage.objects.all())
    name=forms.ChoiceField(choices=nl)
    author=forms.CharField()
    date=forms.DateField()
    


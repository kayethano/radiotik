from django import forms
from django.forms import ModelForm

from radiotik.stations.models import Station

class StationForm(ModelForm):
	class Meta:
		model = Station
		exclude = ('owner')
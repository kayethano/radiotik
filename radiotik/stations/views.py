from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response


from radiotik.stations.forms import StationForm

#Return form for create a new radio station
@login_required(login_url='/')
def create(request):
	if request.method == 'POST':
		form = StationForm(request.POST, request.FILES)
		if form.is_valid():
			station = form.save(commit=False)
			sation.owner = request.user
			station.save()
			return HttpResponseRedirect('/')
	else:
		form = StationForm()
	return render_to_response('stations/create.html',{
		'form':form,
		},
		context_instance=RequestContext(request))

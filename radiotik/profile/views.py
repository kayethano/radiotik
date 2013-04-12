from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from radiotik.profile.forms import ProfileForm
from radiotik.profile.models import Profile

#Return form with profile fields
@login_required(login_url='/')
def edit(request):
	current = get_object_or_404(Profile, user=request.user)
	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES, instance=current)
		if form.is_valid():
			profile = form.save()
			return HttpResponseRedirect('/profile/%s' % (profile.user))
	else:
		ProfileForm(instance=current)
	return render_to_response('profile/edit.html',
		{
		'form':form
		},
		context_instance=RequestContext(request))
			
from django.shortcuts import render
from .forms import ParticipantForm, RegistrationForm
from .models import Participant, Registration
# Create your views here.
def register(request):
	participation_form = ParticipantForm(request.POST)
	registration_form = RegistrationForm(request.POST)

	if registration_form.is_valid():
		registration_form.save()

	if participation_form.is_valid():
		participation_form.save()

	context = { 'participation_form' : participation_form,
		'registration_form' : registration_form, }

	return render(request, 'register.html', context )
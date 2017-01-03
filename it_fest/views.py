from django.shortcuts import render
from .forms import ParticipantForm, RegistrationForm
from .models import Participant, Registration
# Create your views here.
def register(request):
	participation_form = ParticipantForm(request.POST)
	registration_form = RegistrationForm(request.POST)

	if registration_form.is_valid() and participation_form.is_valid():
		registration = registration_form.save()
		participation = participation_form.save(commit=False)
		participation.registration = registration
		participation.save()

	context = { 'participation_form' : participation_form,
		'registration_form' : registration_form, }

	return render(request, './register.html', context )

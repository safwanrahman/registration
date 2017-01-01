from django import forms
from .models import Participant, Registration


class ParticipantForm(forms.ModelForm):
	class Meta:
		model = Participant
		exclude = ['registration']

class RegistrationForm(forms.ModelForm):
	class Meta:
		model = Registration
		fields = '__all__'
		
from django.forms import formset_factory
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import render
from .forms import ParticipantForm, CodParticipantForm, RegistrationForm


def save_participant_form(participant_form, registration, institute=None):
    participant = participant_form.save(commit=False)
    participant.registration = registration
    if institute:
        participant.institute = institute
    return participant.save()

# Create your views here.
def register(request, game):
    GAMES = {
        'nfs': 'Need For Speed',
        'fifa': 'Fifa',
        'cod': 'Call Of Duty 4'
    }
    CodFormset = formset_factory(CodParticipantForm, extra=4,
                                 max_num=4, validate_max=True,
                                 min_num=4, validate_min=True)

    participation_form = ParticipantForm()
    registration_form = RegistrationForm()
    cod_formset = CodFormset()

    try:
        game_name = GAMES[game]
    except KeyError:
        raise Http404('Wrong Game')

    if request.POST:
        participation_form = ParticipantForm(request.POST)
        registration_form = RegistrationForm(request.POST)

        if registration_form.is_valid() and participation_form.is_valid():
            if game == 'cod':
                cod_formset = CodFormset(request.POST)
                if cod_formset.is_valid():
                    # Save the registration object
                    registration = registration_form.save(commit=False)
                    registration.game_name = game
                    registration.save()

                    # Get The institute Name from the leader participant
                    institute = participation_form.cleaned_data['institute']
                    all_participate_forms = cod_formset.forms + [participation_form]
                    # Save all the participant including the leader participant
                    for form in all_participate_forms:
                        save_participant_form(form, registration, institute=institute)
                    # Return to confirm page only if the formset is valid
                    return render(request, './confirm.html',
                                  {'game_name': game_name, 'registration_num': registration.id})
            else:
                registration = registration_form.save(commit=True)
                registration.game_name = game
                registration.save()
                save_participant_form(participation_form, registration)
                return render(request, './confirm.html',
                              {'game_name': game_name, 'registration_num': registration.id})

    context = {'participation_form': participation_form,
               'registration_form': registration_form,
               'game_name': game_name}

    if game == 'cod':
        context['cod_formset'] = cod_formset

    return render(request, './register.html', context)


def home(request):
    return render(request, './index.html')

from django.http import Http404
from django.shortcuts import render
from .forms import ParticipantForm, RegistrationForm


# Create your views here.
def register(request, game):
    GAMES = {
        'nfs': 'Need For Speed',
        'fifa': 'Fifa',
    }

    try:
        game_name = GAMES[game]
    except KeyError:
        raise Http404('Wrong Game')

    if request.POST:
        participation_form = ParticipantForm(request.POST)
        registration_form = RegistrationForm(request.POST)

        if registration_form.is_valid() and participation_form.is_valid():
            registration = registration_form.save()
            participation = participation_form.save(commit=False)
            participation.registration = registration
            participation.game_name = game
            participation.save()
            return render(request, './confirm.html', {'game_name': game_name})



    context = {'participation_form': ParticipantForm(),
               'registration_form': RegistrationForm(),
               'game_name': game_name}

    return render(request, './register.html', context)

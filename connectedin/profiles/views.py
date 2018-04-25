from django.shortcuts import render
from profiles.models import Profile

def index(request):
    return render(request, 'index.html')

def show(request, profile_id):

    profile = Profile()

    if (profile_id == '1'):
        profile = Profile('Vinicius Serpa', 'vinicius-serpa@gmail.com', '991', 'Infinity Loop')

    return render(request, 'profile.html', { "profile": profile })

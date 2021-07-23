from django.shortcuts import render

def profiles(request):
    template = 'profiles/profile.html'
    context = ()

    return render(request, template, context)

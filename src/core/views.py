from django.shortcuts import render


# Create your views here.
def core_view(request):
    return render(request, 'core/index.html', {})


def core_signin(request):
    return render(request, 'core/signin.html', {})


def core_signup(request):
    return render(request, 'core/signup.html', {})


def core_about(request):
    return render(request, 'core/about.html', {})

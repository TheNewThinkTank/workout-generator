from django.shortcuts import render


def welcome_view(request):
    return render(request, "index.html")


def nfp_view(request):
    return render(request, "full_body_1.html")


def legs_view(request):
    return render(request, "legs_workout.html")

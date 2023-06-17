from django.shortcuts import render


def welcome_view(request):
    return render(request, "index.html")


def nfp_view(request):
    return render(request, "pgm4_nfp/full_body_1.html")

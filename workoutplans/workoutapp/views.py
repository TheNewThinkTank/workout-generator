from django.shortcuts import render

programs = [
    {
        "name": "full_body"
    },
    {
        "name": "legs_workout"
    },
        ]


def welcome_view(request):
    context = {
        "programs": programs
    }
    return render(request, "index.html", context)


def nfp_view(request):
    return render(request, "full_body_1.html")


def legs_view(request):
    return render(request, "legs_workout.html")

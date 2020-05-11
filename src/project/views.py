from django.shortcuts import render


def index(request):

    return render(request,
                  template_name="project/index.html")


def living(request):

    return render(request,
                  template_name="project/living.html")


def commercial(request):

    return render(request,
                  template_name="project/commercial.html")


def hotels(request):

    return render(request,
                  template_name="project/hotels.html")

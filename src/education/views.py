from django.shortcuts import render


def index(request):

    return render(request,
                  template_name="education/index.html")


def buspro(request):

    return render(request,
                  template_name="education/buspro.html")


def knx(request):

    return render(request,
                  template_name="education/knx.html")

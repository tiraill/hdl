from django.shortcuts import render


def index(request):

    return render(request,
                  template_name="index.html")


def about(request):

    return render(request,
                  template_name="about.html")


def contacts(request):

    return render(request,
                  template_name="contacts.html")


def support(request):

    return render(request,
                  template_name="support.html")

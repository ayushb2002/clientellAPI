from django.shortcuts import render


def index(request):
    return render(request, "home/index.html")


def docs(request):
    return render(request, "home/docs.html")


def opportunityDocs(request):
    context = {"link": str(request.build_absolute_uri()[
                           :request.build_absolute_uri().find('.com/')+4])}
    return render(request, "home/opportunity.html", context)


def accountsDocs(request):
    context = {"link": str(request.build_absolute_uri()[
                           :request.build_absolute_uri().find('.com/')+4])}
    return render(request, "home/accounts.html", context)


def usersDocs(request):
    context = {"link": str(request.build_absolute_uri()[
                           :request.build_absolute_uri().find('.com/')+4])}
    return render(request, "home/users.html", context)

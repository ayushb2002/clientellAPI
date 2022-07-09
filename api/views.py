from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from api.models import User, Account, Opportunity
from rest_framework.response import Response
from rest_framework.views import APIView
from django.template import *


class UserView(APIView):
    queryset = User.objects.all()

    def get(self, request, page):
        if page < 1:
            return Response({"message": "Please enter a valid page number!"})
        user = User.objects.all()[::-1]
        # if len(user) > 200:
        #     user = user[:200]
        if (page-1)*10 > len(user):
            return Response({"message": "Empty page!"})
        users = {}
        res = {}
        i = 0
        for u in user[(page-1)*10:page*10]:
            i += 1
            res["id"] = u.id
            res["name"] = u.name
            res["amountGreaterThan100000"] = False
            for opp in Opportunity.objects.filter(owner=u):
                if opp.amount > 100000:
                    res["amountGreaterThan100000"] = True
                    break
            users[i] = res
            res = {}

        if (page-1)*10 > 0:
            currentUrl = request.build_absolute_uri()
            prevUrl = currentUrl[:currentUrl.rindex('/')+1]+str(page-1)
            users["previous-page"] = prevUrl

        if (page)*10 < len(user):
            currentUrl = request.build_absolute_uri()
            nextUrl = currentUrl[:currentUrl.rindex('/')+1]+str(page+1)
            users["next-page"] = nextUrl
        # print(nextUrl)
        return Response(users)


# class OpportunityViewSet(viewsets.ModelViewSet):
#     queryset = Opportunity.objects.all()
#     serializer_class = OpportunitySerializer


class OpportunityView(APIView):
    queryset = Opportunity.objects.all()

    def get(self, request, page):
        if page < 1:
            return Response({"message": "Please enter a valid page number!"})
        opportunity = Opportunity.objects.all()[::-1]
        # if len(opportunity) > 200:
        #     opportunity = opportunity[:200]
        if (page-1)*10 > len(opportunity):
            return Response({"message": "Empty page!"})
        res = {}
        opps = {}
        i = (page-1)*10
        for op in opportunity[(page-1)*10:page*10]:
            i += 1
            res['id'] = op.id
            res['name'] = op.name
            res['amount'] = op.amount
            res['account'] = op.account.id
            res['owner'] = op.owner.id
            opps[i] = res
            res = {}

        if (page-1)*10 > 0:
            currentUrl = request.build_absolute_uri()
            prevUrl = currentUrl[:currentUrl.rindex('/')+1]+str(page-1)
            opps["previous-page"] = prevUrl

        if (page)*10 < len(opportunity):
            currentUrl = request.build_absolute_uri()
            nextUrl = currentUrl[:currentUrl.rindex('/')+1]+str(page+1)
            opps["next-page"] = nextUrl

        return Response(opps)


class AccountView(APIView):
    queryset = Account.objects.all()

    def get(self, request, page):
        if page < 1:
            return Response({"message": "Please enter a valid page number!"})
        account = Account.objects.all()[::-1]
        # if len(account) > 200:
        #     account = account[:200]
        if (page-1)*10 > len(account):
            return Response({"message": "Empty page!"})
        res = {}
        accounts = {}
        i = (page-1)*10
        for acc in account[(page-1)*10:page*10]:
            i += 1
            res['id'] = acc.id
            res['name'] = acc.name
            res['opportunityCount'] = len(
                Opportunity.objects.filter(account=acc))
            accounts[i] = res
            res = {}

        if (page-1)*10 > 0:
            currentUrl = request.build_absolute_uri()
            prevUrl = currentUrl[:currentUrl.rindex('/')+1]+str(page-1)
            accounts["previous-page"] = prevUrl

        if (page)*10 < len(account):
            currentUrl = request.build_absolute_uri()
            nextUrl = currentUrl[:currentUrl.rindex('/')+1]+str(page+1)
            accounts["next-page"] = nextUrl
        return Response(accounts)


def AccountRedirect(request):
    return HttpResponseRedirect('/api/accounts/1')


def UserRedirect(request):
    return HttpResponseRedirect('/api/users/1')


def OpportunityRedirect(request):
    return HttpResponseRedirect('/api/opportunity/1')

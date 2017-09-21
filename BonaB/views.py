from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from BonaB.models import *
from rest_framework import viewsets
from BonaB.serializers import *
from rest_framework import permissions
from BonaB.permissions import IsOwnerOrReadOnly
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


# Create your views here.

def login(request) :

    if request.user.is_authenticated :
        return HttpResponseRedirect('/admin/')
    else :

        username = request.POST.get('signin-username', '')
        pwd = request.POST.get('signin-pwd', '')
        user = authenticate(username=username, password=pwd)

        if user is not None:
            auth_login(request, user)
            return render(request, "../templates/admin/index.html")
        else:
            return render(request, "../templates/admin/login.html")




def list_cc(request):

    if request.user.is_authenticated :
        ccList = CryptoCurrency.objects.all()
        return render_to_response("../templates/admin/list-cc.html", {"ccList" : ccList})
    else :
        return HttpResponseRedirect('/')

def dashboard(request) :

    if not request.user.is_authenticated :
        return HttpResponseRedirect('/')
    else :
        return render(request, "../templates/admin/index.html")

def logout(request) :
    auth_logout(request)
    return HttpResponseRedirect('/')

def newCC(request) :
    if request.user.is_authenticated :

        if request.method == 'POST':

            data = dict(request.POST)
            data = list(data.values())

            cc = CryptoCurrency(coin="Utabit", pszTimestamp=data[1][0], maxMoney=data[2][0], nSubsidyHalving=data[3][0],
                                port=data[4][0],
                                nTime=data[5][0], nBits=data[6][0], dnsSeed=data[7][0], cAmountSubsidy=data[8][0],
                                status="Generating Genesis Block ... ", owner=request.user)
            cc.save()

            for i in range(10, len(data)):
                print(data)
                fn = FullNode(ip=data[i][0], cryptoCurrency=cc)
                fn.save()

            return HttpResponseRedirect('/')

        else:
            return render(request, "../templates/admin/newCC.html")


    else :
        return HttpResponseRedirect('/')

def status(request) :

    if request.method == 'POST' :

        data = dict(request.POST)
        data = list(data.values())
        cc = CryptoCurrency(pszTimestamp = data[1][0],maxMoney = data[2][0],nSubsidyHalving = data[3][0],port = data[4][0],
                            nTime = data[5][0],nBits = data[6][0],dnsSeed = data[7][0],cAmountSubsidy = data[8][0], status="Generating Genesis Block ... ")
        cc.save()

        for i in range(10,len(data)):
            print(data)
            fn = FullNode(ip = data[i][0], cryptoCurrency = cc)
            fn.save()

        return HttpResponse("hiii")
    # return render(request,"../templates/status.html")


class CryptoCurrencyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CryptoCurrency.objects.all()
    serializer_class = CryptoCurrencySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FullNodeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = FullNode.objects.all()
    serializer_class = FullNodeSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

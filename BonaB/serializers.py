from BonaB.models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class CryptoCurrencySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = CryptoCurrency
        fields = ('id',  'owner' , 'pszTimestamp', 'maxMoney', 'nSubsidyHalving', 'port', 'nTime', 'nBits', 'dnsSeed', 'cAmountSubsidy' ,'status')


class FullNodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FullNode
        fields = ('id', 'ip', 'cryptoCurrency')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id' , 'url', 'username', 'email', 'groups', 'cryptocurrencies')
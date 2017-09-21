from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CryptoCurrency(models.Model) :
    created_at = models.DateTimeField(auto_now_add=True)
    coin = models.CharField(max_length=50)
    pszTimestamp = models.TextField(max_length=1024)
    maxMoney = models.CharField(max_length=30)
    nSubsidyHalving = models.CharField(max_length=30)
    port = models.CharField(max_length=30)
    nTime = models.CharField(max_length=30)
    nBits = models.CharField(max_length=40)
    dnsSeed = models.CharField(max_length=30)
    cAmountSubsidy = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    owner = models.ForeignKey(User)


class FullNode(models.Model) :
    ip = models.CharField(max_length=45)
    cryptoCurrency = models.ForeignKey(CryptoCurrency, null=True)

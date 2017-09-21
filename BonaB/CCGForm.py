from django import forms

class CCGForm(forms.Form):
    pszTimestamp = forms.CharField(required=True)
    maxMoney = forms.CharField(required=True)
    nSubsidyHalving = forms.CharField(required=True)
    port = forms.IntegerField(required=True)
    nTime = forms.CharField(required=True)
    nBits = forms.CharField(required=True)
    dnsSeed = forms.CharField(required=True)
    cAmountSubsidy = forms.CharField(required=True)
    status = forms.CharField(required=True)

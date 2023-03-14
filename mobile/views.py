from django.shortcuts import render

def Iphone(request):
    d={'model':'Iphone15','processor':'A16'}
    return render(request,'Iphone.html',context=d)

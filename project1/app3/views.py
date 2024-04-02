from django.shortcuts import render

# Create your views here.
def Sample3(request):
    d={'name':'Sanjay','Age':23}
    return render(request,'app3.html',context=d)
from django.shortcuts import render

# Create your views here.
def jinj(request):
    d={'name':'shivam','age':9}
    return render(request,'h1.html',context=d)
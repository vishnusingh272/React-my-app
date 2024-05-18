from django.shortcuts import render
from django.http import HttpResponse


def say_hi(request):
    # return HttpResponse("Hi there!")
      return render (request,'index.html')

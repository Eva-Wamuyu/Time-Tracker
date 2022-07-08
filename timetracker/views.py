from django.shortcuts import render

def notFound(request,exception):

  return render(request,"404.html")
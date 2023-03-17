from django.shortcuts import render

# Create your views here.
def place(request):
    D={'name':'nandeeswar','place':'dressrosa'}
    return render(request,'jinja.html',context=D)


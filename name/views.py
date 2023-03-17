from django.shortcuts import render

# Create your views here.
def name(request):
    D={'name':'nandeeswar','place':'mars'}
    return render(request,'jinja.html',context=D)

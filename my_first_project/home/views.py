from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context={
        'variable': 'Muhammad Zohaib Shahid'
    }
    # return HttpResponse("This is the home page")
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'service.html')

def contact(request):
    return render(request,'contact.html')

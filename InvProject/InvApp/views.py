from django.shortcuts import render,redirect
from .forms import ContactForm
# Create your views here.
run = [
{
'Info':'Contact Info',
'content':'Delivering trusted healthcare solutions with excellence and integrity',
'hours':'Mon - Sun (24 Hours)',
'contact':'+256 741 257 369',
'emails':'doctorsavenue@gmail.com',
'location':'Madera, Western Soroti City',
'title':'Doctors Avenue',
},
]

item = [
{
'title':'DOCTORS AVENUE',
'content':'WE ARE TESTING YOU PLEASE',
'email':'avenuedoctors@gmail.com',
'info':'Contact Info',
'location':'Pamba',
'contact':'07741257369',
},
]
def index(request):   
    context = {
    'post':item
    }    
    return render(request,'files/index.html',context)


def about(request):    
    return render(request,'files/about.html')
    
def element(request):
    context ={
    'post':run
    }
    return render(request,'files/elements.html',context)
    
def contact_view(request):
    return render(request,'files/contact.html')
    
def home_view(request):
    
    return render(request,'files/home.html')
    
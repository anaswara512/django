from django.shortcuts import render,redirect
from .forms import PersonForm
from .models import Person

def Personview(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userlist')
    else:
        form = PersonForm()
    return render(request,'person.html',{'form':form})
    

def userlist(request):
    users = Person.objects.all()
    return render(request,'userlist.html',{'users': users})

# Create your views here.

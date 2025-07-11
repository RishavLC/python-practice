from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .models import Contact
from django.contrib.auth.models import User
from .forms import ContactForm,RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate


# Create your views here.

@login_required

def user_register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)#automatically login after registration
            return redirect('home')
    else:
        form = RegisterForm()
            # return render(request, 'contact/register.html', {'form': form})
        return render(request, 'contact/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, 'contact\login.html',{"error":"Invalid credentials"})
            
    return render(request, 'contact\login.html')

def user_logout(request):
    logout(request)
    return redirect('login')
    
def home(request):
    template = 'contact/home.html'
    user = User.objects.get(id=request.user.id)
    contacts = Contact.objects.filter(added_by=user)
    context = {"contacts": contacts}
    return render(request, template, context)
    
def add_friend(request):
    user = User.objects.get(id=request.user.id)
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            new_friend = form.save(commit = False) 
            new_friend.added_by = request.user
            new_friend.save()
            return redirect('home') 
    else:
        form = ContactForm()
        template = 'contact/add_friend.html'
    return render(request, template, {'form': form}) 

# update form infomation
def update_friend(request, pk):
    contact = get_object_or_404(Contact,pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    else:
        form = ContactForm(instance=contact)
        return render(request,'contact/edit_friend.html',{'form':form})

# delete friends
def friend_delete(request,pk):
    friend = get_object_or_404(Contact,pk=pk)
    if request.method == "POST":
        friend.delete()
        return redirect('home')

    return render(request,'contact/friend_confirm_delete.html',{'friend':friend})


def hello(request):
    return HttpResponse("Hello.")


def hi(request):
    return HttpResponse("hii.")


def hi_name(request, name):
    return HttpResponse(f"hii. {name}")



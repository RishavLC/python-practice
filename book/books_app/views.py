from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Book
# from django.contrib.auth.models import User
from .form import BookForm,RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def home(request):
    
    books = Book.objects.all() 
    template =  'books_app/home.html'
    print(books) 
    return render(request,template,{'books':books})

    
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    
    return render(request, 'books_app/add_book.html', {'form': form})


def update_book(request, pk):
    book = get_object_or_404(Book,pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    else:
        form = BookForm(instance=book)
    return render(request, 'books_app/update_book.html', {'form': form})
        


def delete_book(request,pk):
    book = get_object_or_404(Book,pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('home')
    return render(request,'books_app/delete_book.html',{'book':book})



def hi(request):
    return HttpResponse("Hello, world. You're at the hi page.")


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
        return render(request, 'books_app\register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, 'books_app\login.html',{"error":"Invalid credentials"})
            
    return render(request, 'books_app\login.html')

def user_logout(request):
    logout(request)
    return redirect('login')
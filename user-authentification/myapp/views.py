from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from django.contrib import messages
from .models import Student, IndexText,About, AboutSlide
# from .models import IndexText
# from django.shortcuts import redirect

# Create your views here

def signIn(request):
    if request.method=='POST':
        # if 'signIn'=='signIn':
        username=request.POST['username']
        password=request.POST['password']
    
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            # User is authenticated
            auth.login(request, user)
            return redirect("/")

        else:
            messages.info(request, "credential not satisfied")
            return redirect('signIn')
        
    else:
        return render(request, 'signIn.html')


def signUp(request):
    if request.method=='POST':
        fullNames=request.POST['fullNames']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']
        
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already exist')
                return redirect('signUp')

            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already exist')
                return redirect('signUp')
            
            else:
                #go ahead and create user
                user= User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('signIn')
        else:
            messages.info(request, 'password does not match')
            return redirect('signUp')
    else:
        return render(request, 'signUp.html')        
    # return render(request, 'signUp.html')
    
def about(request):
    about=About.objects.all()
    aboutslide=AboutSlide.objects.all()
    context={
        'about': about,
        'Aboutslide': aboutslide
    }
    
    return render(request, 'about.html', context)

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def services(request):
    # about=IndexText.objects.all()
    about="letstart"
    return render(request, 'services.html', {'about': about})

def team(request):
    return render(request, 'team.html')

def index(request):
    persons=Student.objects.all()
    indexText=IndexText.objects.all()
    
    context={
        'persons':persons,
        'indextext':indexText
        
    }
    
    return render(request, 'index.html', context)

def post(request, pk):
    return render(request, 'post.html', {'pk': pk})
    
def counter(request):
    names=['Kongnyuy', 'Livingston', 'Tardzenyuy', 'Bill', 'Nyuydine']
    return render(request, 'counter.html', {'names': names})





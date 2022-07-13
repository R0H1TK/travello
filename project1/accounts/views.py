from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method=='POST':
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        user=request.POST['username']
        em=request.POST['email']
        pass1=request.POST['password1']
        pass2=request.POST['password2'] 
        
        if pass1==pass2:
            if User.objects.filter(username=user).exists(): 
                messages.info(request,'username or email taken') 
                return redirect('register')
            elif User.objects.filter(email=em).exists():
                messages.info(request,'username or email taken')
                return redirect('register')
            else:
                user =User.objects.create_user(username=user,password=pass1,email=em,first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request,'user created')
                return redirect('login')
        else:
            messages.info(request,'password is not macthing...')
            return redirect('register')
        return redirect('/travello')
    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        usern=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=usern, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/travello')
        else:
            messages.info(request, 'inavlid credenstials')
            return redirect('login')

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/travello')
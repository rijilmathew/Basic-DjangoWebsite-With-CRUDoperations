from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from adapp.models import Student







# Create your views here.
@never_cache
@login_required(login_url='handlelogin')
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')  
@never_cache    
def handlelogin(request):
    if request.user.is_authenticated:
         if request.user.is_superuser:
            return redirect('adindex')
         else:
            return redirect('/')

             
    if request.method == "POST":
        uname = request.POST.get()
        pass1 = request.POST.get("pass1")
        myuser = authenticate(username=uname,password=pass1)
        if myuser:
            login(request, myuser)
            messages.success(request, "Login Success")
            if myuser.is_superuser:
                return redirect('ad"username"index')
            else:
                login(request, myuser)
                messages.success(request, "Login Success")
                return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('/login')
        confirmpassword=request.POST.get("pass2")
        # print(uname,email,password,confirmpassword)
        if password!=confirmpassword:
            messages.warning(request,"Password is Incorrect")
            return redirect('/signup')
        try:
            if User.objects.get(username=uname):
              messages.info(request,"UserName Is Taken")
              return redirect('/signup')
        except:
            pass
    return render(request,'login.html')        
   

    
def handlesignup(request):
    if request.method =="POST":
        uname = request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("pass1")
        try:
             if User.objects.get(email=email):
                messages.info(request,"Email Is Taken")
                return redirect('/signup')
        except:
            pass          

        myuser =User.objects.create_user(uname,email,password)
        # myuser.save()
        student = Student(name=uname, email=email)
        student.save()

        messages.success(request,"SignUp Succes Please Login!")
        return redirect('/login')
    return render(request,'signup.html')  
@login_required(login_url='handlelogin')
@never_cache
def handlelogout(request):
    logout(request)
    messages.info(request,"Logout Success")
    return redirect('/login')
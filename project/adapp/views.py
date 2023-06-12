from django.shortcuts import render,redirect
from.models import Student
# from django.contrib.auth import logout
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache




@never_cache
@login_required(login_url='handlelogin')
def adindex(request):
    if not request.user.is_authenticated:
        return redirect('handlelogin')
    if 'search' in request.GET:
        q=request.GET['search']
        multiple_q =Q(Q(name__icontains=q) | Q(age__icontains=q))
        data =Student.objects.filter(multiple_q)
    # query = request.GET.get('q')
    # if query:
    #     data = Student.objects.filter(name__icontains=query)
    else:    
        data = Student.objects.all()
    context={"data":data}
    # return render(request,"adindex.html",context)
    response = render(request, "adindex.html", context)
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'

    # Set session variable to track authentication status
    request.session['authenticated'] = True
    return response

def insertdata(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        print(name,email,age,gender)  
        query=Student(name=name,email=email,age=age,gender=gender) 
        query.save()
        messages.info(request,"Data Inserted Successfully")
        return redirect('adindex')
    # return render(request,"adindex.html")  
def updatedata(request,id):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender']

        edit=Student.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.gender=gender
        edit.age=age
        edit.save()
        messages.warning(request,"Data Updated Successfully")
        return redirect("adindex")
    d=Student.objects.get(id=id)
    context={"d":d}
    return render(request,"adedit.html",context)

def deletedata(request,id):
    d=Student.objects.get(id=id)
    d.delete()
    messages.error(request,"Data Deleted Successfully")
    return redirect("adindex")


    


def about(request):
    return render(request,"adabout.html")  

def adminlogout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request,"Logout Success")
    else:
        messages.error(request, "You are not logged in")    
    return redirect('/login')    



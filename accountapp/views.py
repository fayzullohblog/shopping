from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from accountapp.models import UserModel
# Create your views here.
# def loginview(request):
    
#     password_error=''
#     if request.method=='POST':
#         username=request.POST.get('username')
#         first_name=request.POST.get('first_name')
#         last_name=request.POST.get('last_name')
#         telephone=request.POST.get('telephone')
#         password=request.POST.get('password')
#         password1=request.POST.get('password1')
        
#         if password==password1  :
#             password_error='this password is same two pasword '

def loginview(request):

    username_password_error=''

    if request.method=='POST':
        
        username=request.POST.get('username')
        password=request.POST.get('password')
        check_usermodel=authenticate(
            username=username,
            password=password,
        )
        print(username,password)
        print('-----',check_usermodel)
        if check_usermodel:
            print(username,password)
            login(request,check_usermodel)
            return redirect('indexview')
        
        else:
            
            username_password_error="you don't register or you forget password "
 

    return render(request=request,template_name='account/login.html',context={'username_password_error':username_password_error})


def registerview(request):
    passworderror=''
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        password1=request.POST.get('password1')
        email=request.POST.get('email')
        telephone=request.POST.get('telephone')
        print('request----',request.POST)
        if password != password1:
            passworderror='you are not the same passwords '



        else:
            user=UserModel.objects.create(
                    username=username,
                    password=password,
                    email=email,
                    telephone=telephone,
                )
            print('email',email)
      
            user.set_password(password)
            user.save()
            return redirect('loginview')
    
    return render(request=request,template_name='account/register.html',context={'passworderror':passworderror})

       
def logoutview(request):
    logout(request=request)
    return redirect('loginview')

     


    

    

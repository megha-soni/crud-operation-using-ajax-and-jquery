from django.shortcuts import render
from django.http import JsonResponse
from .forms import RegisterForm
from .models import User
from django.views.decorators.csrf import csrf_exempt


def Home(request):
    form=RegisterForm()
    details=User.objects.all()
    return render(request, 'app/base.html',{'form':form,'details':details})


# adding csrf_exempt as security exemption for security purpose
@csrf_exempt    
def SaveData(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid:          #checking if form is valid or not
            sid=request.POST['stuid']
            name=request.POST['name']
            email=request.POST['email']
            password=request.POST['password']
            if(sid== ""):
                user=User(name=name,email=email,password=password)  #comparing the data from models
            else :
                user=User(id=sid,name=name,email=email,password=password)
            user.save()
            return JsonResponse({'status':'save'})   
        


@csrf_exempt        
def DeleteData(request):
    if request.method=="POST":
        id=request.POST.get("sid")
        pid=User.objects.get(pk=id)  #getting the perticular data's id for performing delete operation
        pid.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})


@csrf_exempt
def EditData(request):
    if request.method=="POST":
        id=request.POST.get("sid")
        user=User.objects.get(pk=id)
        user_data={"id":user.id,"name":user.name,"email":user.email,"password":user.password}
        return JsonResponse(user_data)
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from CRUDAPP.models import StudentData

def HomePage(request):
    students=StudentData.objects.all()
    return render(request, "homepage.html",{"students":students})

@csrf_exempt
def InsertStudent(request):
    name=request.POST.get("name")
    email=request.POST.get("email")
    gender=request.POST.get("gender")

    try:
        student=StudentData(name=name,email=email,gender=gender)
        student.save()
        student_data={"id":student.id,"created_at":student.created_at,"error":False,"errorMessage":"Student Added Successfully"}
        return JsonResponse(student_data,safe=False)
    except:
        student_data={"error":True,"errorMessage":"Failed to Add Student"}
        return JsonResponse(student_data,safe=False)
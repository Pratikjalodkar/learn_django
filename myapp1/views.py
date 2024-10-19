from django.shortcuts import render, HttpResponse

def home(request):
    data ={
        'title':'Personnel Website',
        'htmldata':'Hii I am Pratik Jalodkar',
        'clist':['JAVA', 'Python', 'Django'],
        'student_details':[
            {'name':'Pratik', 'mobile_no':'1234567890'},
            {'name':'Pramod', 'mobile_no':'2356867890'},
        ]
    }
    return render(request, "index.html", data)

def about(request):
    return HttpResponse("this is about page")

def services(request):
    return HttpResponse("this is services page")

def contact(request):
    return HttpResponse("this is contact page")

def course(request):
    return HttpResponse("this is course page")

def courseDetails(request,courseId):
    return HttpResponse(f"<h1>{courseId}<h1/>")

def htmlRenderPage(request):
    return render(request, "index.html")



from django.shortcuts import render, HttpResponse

# def test(request):
#     data ={
#         'title':'Personnel Website',
#         'htmldata':'Hii I am Pratik Jalodkar',
#         'clist':['JAVA', 'Python', 'Django'],
#         'student_details':[
#             {'name':'Pratik', 'mobile_no':'1234567890'},
#             {'name':'Pramod', 'mobile_no':'2356867890'},
#         ]
#     }
#     return render(request, "index.html", data)

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def contact(request):
    return render(request, "contact.html")

# def course(request):
#     return HttpResponse("this is course page")

# def courseDetails(request,courseId):
#     return HttpResponse(f"<h1>{courseId}<h1/>")

# def htmlRenderPage(request):
#     return render(request, "index.html")




def userForm(request):
    name=''
    email=''
    password=''
    try:
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']

            print(name, email, password)

    except:
        pass

    return render(request, 'userform.html',{'name':name,'email':email,'password':password})


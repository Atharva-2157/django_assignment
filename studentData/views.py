from django.shortcuts import render
from app1.models import student

def homePage(request):
     # Render main page
     return render(request, "HomePage.html")
 
def printData(request):
    # Process form data and display all student records
    if request.method == "POST":
        fname = request.POST.get('fname')
        dob = request.POST.get('dob')
        addr1 = request.POST.get('addr1')
        mno = request.POST.get('mobNo')
        mail = request.POST.get('mail')
        data = student(name=fname, dob=dob, addr1=addr1, mobNo=mno, mail=mail)
        data.save()
        
        data = student.objects.all() 
    return render(request, "HomePage.html", {'printData':data})

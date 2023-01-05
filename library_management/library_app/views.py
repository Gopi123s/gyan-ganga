from django.shortcuts import render,HttpResponse
from .models import *
from datetime import datetime

# Create your views here.
def home(request):
    return render (request,'home.html')

def avl_book(request):
    all_book=Author.objects.all()
    l=Author.objects.all().count()
    # l=[i for i in range(1,count_book+1)]
    print(l)
    d={'all_book':all_book,'l':l}
    return render(request,'avl_book.html',d)

def issue_book(request):
    issue_book=Student.objects.all()
    d={'issue_book':issue_book}
    return render(request,'issue_book.html',d)

def issue_book_student(request):
    
    if request.method =="POST":
        stu_name=request.POST['stu_name']
        father_name=request.POST['father_name']
        address=request.POST['address']
        phone=int(request.POST['phone'])
        book_name=int(request.POST['book_name'])
        author_name=int(request.POST['author_name'])
        print(stu_name)
        new_stu=Student(stu_name=stu_name,father_name=father_name,address=address,phone=phone,book_name_id=book_name,author_name_id=author_name,issue_date=datetime.now())
        new_stu.save()
        print(new_stu)
        return HttpResponse("employee added succsessfully")
    elif request.method=="GET":
        all_book=Author.objects.all()
        d={'all_book':all_book}
        return render(request,'issue_book_student.html',d)
    else:
        
        return HttpResponse("error ocured")


        
    # return HttpResponse ("u have error")        
    all_book=Author.objects.all()
    d={'all_book':all_book}
    return render(request,'issue_book_student.html',d)

def delete(request,stu_id):
    # if request.method=="POST":
    #     stu_id=request.POST['stu_id']
    if stu_id:
        try:
            del_stu=Student.objects.get(id=stu_id)
            del_stu.delete()
            return HttpResponse("deleted")
        except:
            return  HttpResponse("somthing Went Wrong")

        
    return HttpResponse ("try again")

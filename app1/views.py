from django.shortcuts import render,redirect
from .models import login,add,borrow
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth import logout,authenticate
from django.contrib import messages
from .forms import edit_bookform,EditprofileForm,ChangepasswordForm
from datetime import datetime
# Create your views here.
def display(request):
    return render(request,'reg.html')
def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        classs = request.POST['classs']
        password = request.POST['password']
        data = login.objects.create(name=name,phone_number=phone_number,classs=classs,type=0,password=password)
        data.save()
        return render(request,'login.html')

def log(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        print(name)
        try:
            data = login.objects.get(name=name)
            if data.password == password:
                request.session['id'] = data.id
                if data.type =='0':
                    return redirect(profile)
                elif data.type == '1':
                    return redirect(liberain)
                else:
                    return HttpResponse("user not found")
            else:
                return HttpResponse("password error")
        except Exception:
            return HttpResponse("error")
    return render(request,'login.html')



def addbook(request):
    if request.method == 'POST':
        book_name = request.POST['book_name']
        auther_name = request.POST['auther_name']
        type_book = request.POST['type_book']
        details= request.POST['details']
        book_photo= request.FILES['book_photo']
        data2 = add.objects.create(book_name=book_name,auther_name=auther_name,type_book=type_book,details=details,image=book_photo)
        data2.save()
        return redirect(liberain)
    else:
        return render(request,'add.html')

def liberain(request):
    data = add.objects.all()
    user_id= request.session['id']
    user=login.objects.get(id=user_id)
    print(user)
    return render(request, 'liberry.html', {'data': data,'user':user})

        

def edit_book(request,id):
    book = add.objects.get(id=id)
    form = edit_bookform(instance=book)
    if request.method == 'POST':
        form = edit_bookform(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect(liberain)

    else:
        return render(request,'edit.html',{'form':form, 'book':book})

def book_details(request,id):
    data = add.objects.get(id=id)
    context = {'data':data}

    return render(request,'bookdetails.html',context)

def profile(request):
    list_book=add.objects.all()
    user_id = request.session['id']
    user = login.objects.get(id=user_id)
    return render(request,'studentportel.html',{'list_book':list_book,'user':user})


def logout_view(request):
    logout(request)
    messages.success(request, ("you were logged out !"))
    return redirect('home')

def delete_book(request,id):
    book = add.objects.get(id=id)
    book.delete()
    return redirect(liberain)

def search_book(request):
    if request.method == "GET":
        search = request.GET.get('search')
        post = add.objects.all().filter(book_name__icontains=search)
        print(post)
        return render(request,'studentportel.html',{'post':post})

def chnage_passwordpro(request,id):
    user = login.objects.get(id=id)
    form = ChangepasswordForm(instance=user)
    if request.method == 'POST':
        form = ChangepasswordForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect(profile)

    else:
        return render(request,'profile-pc.html',{'form':form, 'user':user})


def edit_profileLib(request,id):
    user = login.objects.get(id=id)
    form = EditprofileForm(instance=user)
    print(user)
    if request.method =='POST':
        form = EditprofileForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect(liberain)

    else:
        return render(request,'editprofile.html',{"form":form, "user":user})


def edituserprofile(request,id):
    user1 = login.objects.get(id=id)
    form = EditprofileForm(instance=user1)
    if request.method =='POST':
        form = EditprofileForm(request.POST,instance=user1)
        if form.is_valid():
            form.save()
            return redirect(profile)

    else:
        return render(request,'edituserprofile.html',{"form":form, "user1":user1})


def chnage_passwordlib(request,id):
    user = login.objects.get(id=id)
    form = ChangepasswordForm(instance=user)
    if request.method == 'POST':
        form = ChangepasswordForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect(liberain)

    else:
        return render(request,'libery-pc.html',{'form':form, 'user':user})


def borrow_book(request,id):
    user_id = request.session['id']
    user = login.objects.get(id=user_id)
    book = add.objects.get(id = id)

    if request.method=='POST':
        book_id = request.POST.get('book_id')
        current_book = add.objects.get(id=book_id)
        data = borrow.objects.create(user=user,book_id=current_book)
        data.save()
        return HttpResponse("BOOKED SUCCESSFULLY")
    else:
        return render(request,'studentportel.html',{'book':book})

def historylib(request):
    history=borrow.objects.all()
    user_id = request.session['id']
    user = login.objects.get(id=user_id)
    return render(request,'history_lib.html',{'history':history,'user':user})

def historyuser(request):
    user_id = request.session['id']
    user = login.objects.get(id=user_id)
    data = borrow.objects.filter(user=user)
    return render(request,'history_profile.html',{'data':data, 'user_id':user})


def return_book(request,id):
    if 'id' in request.session:
        data1 = borrow.objects.get(id=id)
        data1.delete()
        return redirect(historyuser)
    else:
        return redirect(profile)


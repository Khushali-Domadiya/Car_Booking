from django.shortcuts import render, redirect
from django.core.mail import send_mail
from car_rent import settings
# from admin_side.models import sign_up,SIGN_UP,team,TEAM,car_category,CAR_CATEGORY
from admin_side.models import *
from frontend.models import *

# Create your views here.


def dashboard(request):
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).get()
    else:
        return redirect('/myadmin/sign_in/')
    slide_count = slide.objects.count()
    car_category_count = car_category.objects.count()
    car_brand_count = brand.objects.count()
    car_count = car.objects.count()
    return render(request, 'dashboard.html', {'row': row,'slide_count':slide_count,'car_category_count':car_category_count,'car_brand_count':car_brand_count,'car_count':car_count})

def sign_in_admin(request):
    msg = ''
    if 'save' in request.POST:
        email = request.POST['email']
        password = request.POST['password']

        data = sign_up.objects.filter(email=email, password=password)
        if data.count() == 1:
            row = data.first()
            request.session['admin_id'] = row.id

            subject = "Log in"
            msg = "Congratulations for your successlly Login"

            res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [email])
            if (res == 1):
                msg = "Mail Sent Successfuly"
                return redirect('/myadmin/dashboard/')
            else:
                msg = "Mail could not sent"
        else:
            msg = 'Please Enter Valid Email Or Password'
    return render(request, 'signin.html', {'msg': msg})


def sign_up_admin(request):
    msg = ''
    frm = SIGN_UP
    if 'save' in request.POST:
        frm = SIGN_UP(request.POST, request.FILES)
        email = request.POST['email']
        subject = "Log in"
        msg = "Congratulations for your successlly Login"

        res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [email])
        if (res == 1):
            msg = "Mail Sent Successfuly"
        else:
            msg = "Mail could not sent"
        frm.save()
    return render(request, 'signup.html', {'msg': msg})


def log_out_admin(request):
    del request.session['admin_id']
    return redirect('/myadmin/sign_in/')


def add_team(request):
    row = ''
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).first()

    if 'save' in request.POST:
        tem = TEAM(request.POST, request.FILES)
        tem.save()
    return render(request, 'add_team.html', {'row': row})


def manage_team(request):
    row = ''
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).first()
    else:
        return redirect('/myadmin/sign_in')
    data = team.objects.all()
    return render(request, 'manage_team.html', {'data': data, 'row': row})


def update_team(request, edit):
    row = ''
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).first()
    else:
        return redirect('/myadmin/sign_in')
    data = team.objects.filter(id=edit).get()
    if 'save' in request.POST:
        frm = TEAM(request.POST, request.FILES, instance=data)
        frm.save()
        return redirect('/myadmin/manage_team/')
    return render(request, 'add_team.html', {'data': data, 'row': row})

def delete_team(request, delt):
    data = team.objects.filter(id=delt).delete()
    return redirect('/myadmin/manage_team')


def add_category(request):
    row = ''
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).first()
    else:
        return redirect('/myadmin/sign_in')
    if 'save' in request.POST:
        frm = CAR_CATEGORY(request.POST, request.FILES)
        frm.save()
    return render(request, 'add_category.html', {'row': row})

def manage_category(request):
    row = ''
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).first()
    else:
        return redirect('/myadmin/sign_in')
    data = car_category.objects.all()
    return render(request, 'manage_category.html', {'data': data, 'row': row})

def update_category(request, edit):
    row = ''
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).first()
    else:
        return redirect('/myadmin/sign_in')
    data = car_category.objects.filter(id=edit).get()
    if 'save' in request.POST:
        frm = CAR_CATEGORY(request.POST, request.FILES, instance=data)
        frm.save()
        return redirect('/myadmin/manage_category/')
    return render(request, 'add_category.html', {'data': data, 'row': row})

def delete_category(request, delt):
    data = car_category.objects.filter(id=delt).delete()
    return redirect('/myadmin/manage_category/')

def add_brand(request):
    row = ''
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).first()
    else:
        return redirect('/myadmin/sign_in')
    if 'save' in request.POST:
        frm = BRAND(request.POST, request.FILES)
        frm.save()
    return render(request, 'add_brand.html', {'row': row})

def manage_brand(request):
    row = ''
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).first()
    else:
        return redirect('/myadmin/sign_in')
    data = brand.objects.all()
    return render(request, 'manage_brand.html', {'data': data, 'row': row})

def update_brand(request, edit):
    row = ''
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).first()
    else:
        return redirect('/myadmin/sign_in')
    data = brand.objects.filter(id=edit).get()
    if 'save' in request.POST:
        frm = BRAND(request.POST, request.FILES, instance=data)
        frm.save()
        return redirect('/myadmin/manage_brand')
    return render(request, 'add_brand.html', {'row': row, 'data': data})

def delete_brand(request, delt):
    data = brand.objects.filter(id=delt).delete()
    return redirect('/myadmin/manage_brand')

def add_car(request):
    row = ''
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).first()
    else:
        return redirect('/myadmin/sign_in')
    cat = car_category.objects.all()
    brd = brand.objects.all()
    frm = CAR()
    if 'save' in request.POST:
        frm = CAR(request.POST, request.FILES)
        if frm.is_valid():
            frm.save()
        print('successss')
    return render(request, 'add_car.html', {'cat': cat, 'row': row, 'brd': brd, 'form': frm})

def manage_car(request):
    row = ''
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).first()
    else:
        return redirect('/myadmin/sign_in')
    data = car.objects.all()
    return render(request,'manage_car.html',{'row':row,'data':data})

def update_car(request,edit):
    row = ''
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).first()
    else:
        return redirect('/myadmin/sign_in')
    data = car.objects.filter(id=edit).get()
    cat = car_category.objects.all()
    brd = brand.objects.all()
    if 'save' in request.POST:
        frm = CAR(request.POST,request.FILES,instance=data)
        frm.save()
        return redirect('/myadmin/manage_car')
    return render(request,'add_car.html',{'row':row,'data':data,'cat':cat,'brd':brd})

def delete_car(request,delt):
    data = car.objects.filter(id=delt).delete()
    return redirect('/myadmin/manage_car')

def add_slide(request):
    row = ''
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).first()
    else:
        return redirect('/myadmin/sign_in')
    if 'save' in request.POST:
        sld = SLIDE(request.POST,request.FILES)
        sld.save()
    return render(request, 'add_slide.html',{'row':row})

def manage_slide(request):
    row = ''
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).first()
    else:
        return redirect('/myadmin/sign_in')
    data = slide.objects.all()
    return render(request,'manage_slide.html',{'row':row,'data':data})

def update_slide(request,edit):
    row = ''
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).first()
    else:
        return redirect('/myadmin/sign_in')
    data = slide.objects.filter(id=edit).get()
    if 'save' in request.POST:
        frm = SLIDE(request.POST,request.FILES,instance=data)
    return render(request,'add_slide.html',{'row':row,'data':data})

def delete_slide(request,delt):
    data = slide.objects.filter(id=delt).delete()
    return redirect('/myadmin/manage_slide')

def my_profile(request):
    row = ''
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).first()
        
    else:
        return redirect('/myadmin/sign_in')
    data = sign_up.objects.filter(id=request.session['admin_id']).all()
    return render(request,'myprofile.html',{'row':row,'data':data})

def manage_review(request):
    row = ''
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).first()
    else:
        return redirect('/myadmin/sign_in')
    data = review.objects.all()
    return render(request,'manage_review.html',{'row':row,'data':data})

def manage_contact(request):
    row = ''
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).first()
    else:
        return redirect('/myadmin/sign_in')
    data = contact.objects.all()
    return render(request,'manage_contact.html',{'row':row,'data':data})

def manage_user(request):
    data = signup.objects.all()
    return render(request,'manage_user.html',{'data':data})
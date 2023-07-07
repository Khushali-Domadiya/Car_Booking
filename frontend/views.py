from django.shortcuts import render,redirect
from car_rent import settings
from django.core.mail import send_mail
from frontend.models import *
from admin_side.models import *
import random

# Create your views here.
def home(request):
    row = ''
    msg = ''
    if 'user_id' in request.session:
        row = signup.objects.filter(id=request.session['user_id']).get()
    if 'save' in request.POST:
        cont = CONTACT(request.POST)
        email = request.POST['email']
        cont.save()
        subject = 'Thank you'
        msg = 'thank you for contact us'
        res = send_mail(subject,msg,settings.EMAIL_HOST_USER,[email])
        if (res == 1):
            msg = 'Mail Sent Successfully'
        else:
            msg = 'Something Went Wrong'
    sld = slide.objects.all()
    all_car = car.objects.all()
    tem = team.objects.all()
    brd = brand.objects.all()    
    car_pick = car.objects.order_by('id').all()[:6]
    all_review = review.objects.filter(status=1).all()
    return render(request,'index.html',{'row':row,'msg':msg,'sld':sld,'all_car':all_car,'tem':tem,'brd':brd,'all_review':all_review,'car_pick':car_pick})

def about(request):
    row = ''
    if 'user_id' in request.session:
        row = signup.objects.filter(id=request.session['user_id']).get()
    all_car = car.objects.all()
    brd = brand.objects.all()
    car_pick = car.objects.order_by('id').all()[:6]
    return render(request,'about.html',{'row':row,'all_car':all_car,'brd':brd})

def service(request):
    row = ''
    if 'user_id' in request.session:
        row = signup.objects.filter(id=request.session['user_id']).get()
    all_car = car.objects.all()
    car_pick = car.objects.order_by('id').all()[:6]
    return render(request,'service.html',{'row':row,'all_car':all_car})

def contact_fe(request):
    row = ''
    if 'user_id' in request.session:
        row = signup.objects.filter(id=request.session['user_id']).get()
    all_car = car.objects.all()
    brd = brand.objects.all()
    msg = ''
    if 'save' in request.POST:
        cont = CONTACT(request.POST)
        email = request.POST['email']
        cont.save()
        subject = 'Thank you'
        msg = 'thank you for contact us'
        res = send_mail(subject,msg,settings.EMAIL_HOST_USER,[email])
        if (res == 1):
            msg = 'Mail Sent Successfully'
        else:
            msg = 'Something Went Wrong'
    car_pick = car.objects.order_by('id').all()[:6]
    return render(request,'contact.html',{'row':row,'all_car':all_car,'brd':brd,'msg':msg})

def car_listing(request):
    row = ''
    if 'user_id' in request.session:
        row = signup.objects.filter(id=request.session['user_id']).get()
    all_car = car.objects.all()
    brd = brand.objects.all()
    car_pick = car.objects.order_by('id').all()[:6]

    return render(request,'car_listing.html',{'row':row,'all_car':all_car,'brd':brd})

def car_detail(request):
    row = ''
    if 'user_id' in request.session:
        row = signup.objects.filter(id=request.session['user_id']).get()

    car_det = car.objects.order_by('-id').all()[:1]
    all_car = car.objects.all()
    brd = brand.objects.all()
    car_pick = car.objects.order_by('id').all()[:6]

    return render(request,'car_detail.html',{'row':row,'all_car':all_car,'brd':brd,'car_det':car_det})

def car_booking(request):
    row = ''
    if 'user_id' in request.session:
        row = signup.objects.filter(id=request.session['user_id']).get()
    all_car = car.objects.all()
    brd = brand.objects.all()
    car_data = car.objects.order_by('-id').all()[:1]
    car_pick = car.objects.order_by('id').all()[:6]

    return render(request,'car_booking.html',{'row':row,'all_car':all_car,'brd':brd,'car_data':car_data})

def car_team(request):
    row = ''
    if 'user_id' in request.session:
        row = signup.objects.filter(id=request.session['user_id']).get()
    all_car = car.objects.all()
    brd = brand.objects.all()
    all_team = team.objects.all()
    car_pick = car.objects.order_by('id').all()[:6]
    return render(request,'our_team.html',{'row':row,'all_car':all_car,'brd':brd,'all_team':all_team})

def testimonial(request):
    row = ''
    if 'user_id' in request.session:
        row = signup.objects.filter(id=request.session['user_id']).get()
    all_car = car.objects.all()
    brd = brand.objects.all()
    rev = review.objects.all()
    return render(request, 'testimonial.html',{'row':row,'all_car':all_car,'brd':brd,'rev':rev})

def registration(request):
    row = ''
    if 'user_id' in request.session:
        row = signup.objects.filter(id=request.session['user_id']).get()
    msg = ''
    # frm = SIGNUP
    if 'save' in request.POST:
        old_email = request.POST['email']
        emails = signup.objects.filter(email=old_email).all()
        if emails.count() == 1:
            msg = 'Plaese Enter Another Email'
        else:
            frm = SIGNUP(request.POST, request.FILES)
            frm.save()
            email = request.POST['email']
            subject = 'Registration'
            msg = 'SuccessFully Registration in Royal Cars'
            res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [email])
            if (res == 1):
                msg = 'Mail sent Successfully'
            else:
                msg = 'something Went Wrong'
    all_car = car.objects.all()
    brd = brand.objects.all()
    car_pick = car.objects.order_by('id').all()[:6]
    return render(request,'registration.html',{'msg':msg,'all_car':all_car,'brd':brd,'row':row})

def log_in(request):
    row = ''
    if 'user_id' in request.session:
        row = signup.objects.filter(id=request.session['user_id']).get()
    msg = ''
    if 'save' in request.POST:
        email = request.POST['email']
        password = request.POST['password']

        data = signup.objects.filter(email=email,password=password)
        print(data.count())
        if data.count() == 1:
            row = data.first()
            request.session['user_id'] = row.id

            subject = "Log in"
            msg = "Congratulations for your successlly Login"

            res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [email])
            if (res == 1):
                msg = "Mail Sent Successfuly"
                return redirect('/')
            else:
                msg = "Mail could not sent"
        else:
            msg = 'Please Enter Valid Email Or Password'
    all_car = car.objects.all()
    brd = brand.objects.all()
    car_pick = car.objects.order_by('id').all()[:6]
    return render(request,'log_in.html',{'msg':msg,'all_car':all_car,'brd':brd,'row':row})

def log_out(request):
    del request.session['user_id']
    return redirect('/')

def edit_profile(request):
    row = ''
    if 'user_id' in request.session:
        row = signup.objects.filter(id=request.session['user_id']).get()
    data = signup.objects.filter(id=request.session['user_id']).first()
    if 'save' in request.POST:
        frm = SIGNUP(request.POST, request.FILES, instance=data)
        frm.save()
    all_car = car.objects.all()
    brd = brand.objects.all()
    car_pick = car.objects.order_by('id').all()[:6]
    return render(request,'registration.html',{'data':data,'all_car':all_car,'brd':brd,'row':row})

def send_mail_for_otp(request):
    row = ''
    if 'user_id' in request.session:
        row = signup.objects.filter(id=request.session['user_id']).get()
    msg = ''
    if 'save' in request.POST:
        email = request.POST['email']

        data = signup.objects.filter(email=email).all()
        # print(data)
        if data.count() == 1:
            subject = 'OTP For New Password'
            otp = str(random.randint(100000,999999))
            request.session['otp'] = otp
            msg = 'OTP For your New Password is '+otp+' Dont Share it to Anyone'
            res = send_mail(subject,msg,settings.EMAIL_HOST_USER,[email])
            if (res == 1):
                msg = 'Mail Sent Successfully'
                return redirect('/confirm_otp')
            else:
                msg = 'Mail Couldnot SenT'
    all_car = car.objects.all()
    brd = brand.objects.all()
    car_pick = car.objects.order_by('id').all()[:6]
    return render(request,'send_mail.html',{'msg':msg,'all_car':all_car,'brd':brd,'row':row})

def confirm_otp(request):
    row = ''
    if 'user_id' in request.session:
        row = signup.objects.filter(id=request.session['user_id']).get()
    msg = ''
    otp = request.session['otp']
    if 'save' in request.POST:
        cnf_otp = request.POST['otp']
        if otp == cnf_otp:
            return redirect('/forget_password/')
        else:
            msg = 'Please Enter Valid OTP'
    all_car = car.objects.all()
    brd = brand.objects.all()
    car_pick = car.objects.order_by('id').all()[:6]
    return render(request,'confirm_otp.html',{'msg':msg,'all_car':all_car,'brd':brd,'row':row})

def forget_password(request):
    row = ''
    if 'user_id' in request.session:
        row = signup.objects.filter(id=request.session['user_id']).get()
    if 'save' in request.POST:
        email = request.POST['email']
        new_password = request.POST['new_password']

        data_pswd = signup.objects.filter(email=email).all()
        data_pswd.update(password=new_password)
    all_car = car.objects.all()
    brd = brand.objects.all()
    car_pick = car.objects.order_by('id').all()[:6]
    return render(request,'forget_password.html',{'all_car':all_car,'brd':brd,'row':row})

def details_car(request,car_id):
    row = ''
    if 'user_id' in request.session:
        row = signup.objects.filter(id=request.session['user_id']).get()
    car_data = car.objects.filter(id=car_id).all()
    brd = brand.objects.all()
    subject = ''
    msg = ''
    if 'save' in request.POST:
        frm = BOOKING_DETAIL(request.POST)
        email = request.POST['email']
        drop_time = request.POST['drop_time']
        pickup_date = request.POST['pickup_date']
        name = request.POST['name']
        pick_up = request.POST['pick_up']
        drop = request.POST['drop']
        frm.save()
        subject = "For Book Your Ride In ROYAL CARS"
        msg = "Hello "+name+"This Mail is For Book Your Ride In ROYAL CARS on date"+pickup_date+" On time "+drop_time+" On Pick up Location "+pick_up+" And Drop Location "+drop+" Thank You for Book Your ride"
        res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [email])
        if (res == 1):
            msg = "Mail Sent Successfuly"
        else:
            msg = "Mail could not sent"

    if 'submit' in request.POST:
        frm = REVIEW(request.POST,request.FILES)
        frm.save()
    car_pick = car.objects.order_by('id').all()[:6]
    return render(request,'Details_car.html',{'car_data':car_data,'brd':brd,'msg':msg,'car_id':car_id,'row':row,'car_pick':car_pick})

def search_car(request):
    row = ''
    if 'user_id' in request.session:
        row = signup.objects.filter(id=request.session['user_id']).get()
    car_data = ''
    same_car  = ''
    if 'save' in request.POST:
        car_name = request.POST['car_name']
        car_data = car.objects.filter(id=car_name).all()
    msg = 'No Data Shown'
    all_car = car.objects.all()
    brd = brand.objects.all()
    car_pick = car.objects.order_by('id').all()[:6]
    return render(request,'search_car.html',{'car_data':car_data,'all_car':all_car,'msg':msg,'brd':brd,'same_car':same_car,'row':row,'car_pick':car_pick})

def brand_car(request,brand_id):
    row = ''
    if 'user_id' in request.session:
        row = signup.objects.filter(id=request.session['user_id']).get()
    car_data = car.objects.filter(car_brand_id=brand_id).all()
    brd = brand.objects.all()
    all_car = car.objects.all()
    car_pick = car.objects.order_by('id').all()[:6]
    return render(request,'brand_car.html',{'car_data':car_data,'brd':brd,'all_car':all_car,'row':row,'car_pick':car_pick})

def change_password(request):
    row = ''
    msg = ''
    if 'user_id' in request.session:
        row = signup.objects.filter(id=request.session['user_id']).get()
    if 'save' in request.POST:
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        conf_password = request.POST['conf_password']
        data = signup.objects.filter(password=old_password).all()
        print(data)
        if data.count() == 1:
            if new_password == conf_password:
                data.update(password=new_password)
                return redirect('/')
            else:
                msg = 'New Password and confirm Password Doesnot match'
        else:
            msg = 'Invalid Old Password'
    brd = brand.objects.all()
    car_pick = car.objects.order_by('id').all()[:6]
    return render(request,'change_password.html',{'row':row,'msg':msg,'brd':brd,'car_pick':car_pick})
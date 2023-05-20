from django.shortcuts import render,redirect
from car_rent import settings
from django.core.mail import send_mail
from frontend.models import signup, SIGNUP,contact,CONTACT
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
    return render(request,'index.html',{'row':row,'msg':msg})

def about(request):
    row = ''
    if 'user_id' in request.session:
        row = signup.objects.filter(id=request.session['user_id']).get()
    return render(request,'about.html',{'row':row})

def service(request):
    row = ''
    if 'user_id' in request.session:
        row = signup.objects.filter(id=request.session['user_id']).get()
    return render(request,'service.html',{'row':row})

def contact_fe(request):
    row = ''
    if 'user_id' in request.session:
        row = signup.objects.filter(id=request.session['user_id']).get()
    return render(request,'contact.html',{'row':row})

def car_listing(request):
    row = ''
    if 'user_id' in request.session:
        row = signup.objects.filter(id=request.session['user_id']).get()
    return render(request,'car_listing.html',{'row':row})

def car_detail(request):
    row = ''
    if 'user_id' in request.session:
        row = signup.objects.filter(id=request.session['user_id']).get()
    return render(request,'car_detail.html',{'row':row})

def car_booking(request):
    row = ''
    if 'user_id' in request.session:
        row = signup.objects.filter(id=request.session['user_id']).get()
    return render(request,'car_booking.html',{'row':row})

def car_team(request):
    row = ''
    if 'user_id' in request.session:
        row = signup.objects.filter(id=request.session['user_id']).get()
    return render(request,'our_team.html',{'row':row})

def testimonial(request):
    row = ''
    if 'user_id' in request.session:
        row = signup.objects.filter(id=request.session['user_id']).get()
    return render(request, 'testimonial.html',{'row':row})

def registration(request):
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
        
    return render(request,'registration.html',{'msg':msg})

def log_in(request):
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
    return render(request,'log_in.html',{'msg':msg})

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
    return render(request,'registration.html',{'data':data})


def send_mail_for_otp(request):
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
    return render(request,'send_mail.html',{'msg':msg})

def confirm_otp(request):
    msg = ''
    otp = request.session['otp']
    if 'save' in request.POST:
        cnf_otp = request.POST['otp']

        if otp == cnf_otp:
            return redirect('/forget_password/')
        else:
            msg = 'Please Enter Valid OTP'
    return render(request,'confirm_otp.html',{'msg':msg})

def forget_password(request):
    if 'save' in request.POST:
        email = request.POST['email']
        new_password = request.POST['new_password']

        data_pswd = signup.objects.filter(email=email).all()
        data_pswd.update(password=new_password)
    return render(request,'forget_password.html')
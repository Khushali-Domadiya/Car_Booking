"""car_rent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
# from frontend.views import home,about,service,contact_fe,car_listing,car_detail,car_booking,car_team,testimonial,registration,log_in,send_mail_for_otp,log_out,edit_profile,forget_password,confirm_otp
# from admin_side.views import dashboard,sign_in_admin,sign_up_admin,log_out_admin,add_car,add_team,manage_team,add_slide,add_category,manage_category,update_team,delete_team,update_category,delete_category
from frontend.views import *
from admin_side.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('about/', about),
    path('service/', service),
    path('contact/', contact_fe),
    path('car_listing/', car_listing),
    path('car_detail/', car_detail),
    path('car_booking/', car_booking),
    path('details_car/<int:car_id>', details_car),
    path('car_team/', car_team),
    path('testimonial/', testimonial),
    path('registration/', registration),
    path('search_car/', search_car),
    path('brand_car/<int:brand_id>',brand_car),
    path('log_in/', log_in),
    path('send_mail_for_otp/', send_mail_for_otp),
    path('confirm_otp/', confirm_otp),
    path('forget_password/', forget_password),
    path('log_out/', log_out),
    path('edit_profile/', edit_profile),
    path('change_password/', change_password),
    path('myadmin/my_profile/', my_profile),
    path('myadmin/dashboard/', dashboard),
    path('myadmin/add_slide/', add_slide),
    path('myadmin/manage_slide/', manage_slide),
    path('myadmin/update_slide/<int:edit>', update_slide),
    path('myadmin/add_car/', add_car),
    path('myadmin/manage_car/', manage_car),
    path('myadmin/update_car/<int:edit>', update_car),
    path('myadmin/delete_car/<int:delt>', delete_car),
    path('myadmin/add_category/', add_category),
    path('myadmin/manage_category/', manage_category),
    path('myadmin/update_category/<int:edit>', update_category),
    path('myadmin/delete_category/<int:delt>', delete_category),
    path('myadmin/change_password_ad/', change_password_ad),
    path('myadmin/add_brand/', add_brand),
    path('myadmin/manage_brand/', manage_brand),
    path('myadmin/delete_brand/<int:delt>', delete_brand),
    path('myadmin/update_brand/<int:edit>', update_brand),
    path('myadmin/add_team/', add_team),
    path('myadmin/manage_review/', manage_review),
    path('myadmin/manage_contact/', manage_contact),
    path('myadmin/manage_user/', manage_user),
    path('myadmin/manage_team/', manage_team),
    path('myadmin/update_team/<int:edit>', update_team),
    path('myadmin/delete_team/<int:delt>', delete_team),
    path('myadmin/review_approve/<int:app>', review_approve),
    path('myadmin/review_disapprove/<int:disapp>', review_disapprove),
    path('myadmin/user_block/<int:block>', user_block),
    path('myadmin/user_unblock/<int:unblock>', user_unblock),
    path('myadmin/sign_in/', sign_in_admin),
    path('myadmin/sign_up/', sign_up_admin),
    path('myadmin/search_car_admin/', search_car_admin),
    path('myadmin/log_out_admin/', log_out_admin),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

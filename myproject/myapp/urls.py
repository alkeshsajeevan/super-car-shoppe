from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('cars/',views.cars,name="cars"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('register/',views.register,name="register"),
    path('logi/',views.login,name="login"),
    path('detail/<int:id>',views.car_detail,name="detail"),
    path('search/',views.search,name="search")
   
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

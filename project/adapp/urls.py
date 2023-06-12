from django.urls import path
from adapp import views
# from adapp.views import index
# app_name = 'adapp'

urlpatterns = [
 path('adindex',views.adindex,name="adindex"),
 path('about',views.about,name="about"),
 path('insert',views.insertdata,name="insertdata"),
 path('update/<id>',views.updatedata,name="updatedata"),
 path('delete/<id>',views.deletedata,name="deletedata"),
 path('adminlogout',views.adminlogout,name="adminlogout"),

]
from django.db.models import   Count
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.views import View
from .models import Product
from .forms import CustomerRegistrationForm , CustomerProfileForm , Customer
from django.contrib import messages
# Create your views here.

def ecommerce_project(request):
   template = loader.get_template('home.html')
   return HttpResponse(template.render())

def ecommerce_project(request):
   template = loader.get_template('about.html')
   return HttpResponse(template.render())

def ecommerce_project(request):
   template = loader.get_template('contact.html')
   return HttpResponse(template.render())

class CategoryView(View):
    def get(self, request,val):
       product = Product.objects.filter(category=val)
       title = Product.objects.filter(Category=val).values('title')
       return render(request,"templates/category.html",locals())

class CategoryTitle(View):
    def get(self, request,val):
       product = Product.objects.filter(category=val)
       title = Product.objects.filter(Category=product[0].category).values('title')
       return render(request,"templates/category.html",locals())
    

class ProductDetails(View):
   def get(self,request,pk):
      product = Product.objects.get(pk=pk)
      return render(request,"templates/Productdetails.html",locals())
   
class customerRegistrationview(View):
   def get(self,request):
      form = CustomerRegistrationForm
      return render(request,"templates/customerregistration.html",locals())
   def post(self,request):
      form = CustomerRegistrationForm(request.POST)
      if form.is_valid():
         form.save()
         messages.success(request,"Congratulations! user registered successfully")
      else:
         messages.warning(request,"Invalid Data input")
      return render(request,"templates/customerregistration.html",locals())


class ProfileView(View):
   def get(self,request):
    return render(request,"templates/profile.html",locals())
   def post(self,request):
     form = CustomerProfileForm(request.POST)
     if form.is_valid():
        user = request.user
        name = form.cleaned_data['name']
        locality = form.cleaned_data['locality'] 
        city = form.cleaned_data['city'] 
        mobile = form.cleaned_data['mobile'] 
        state = form.cleaned_data['state'] 
        zipcode = form.cleaned_data['zipcode']

        reg = Customer(user=user,name=name,locality=locality,city=city,mobile=mobile,state=state,zipcode=zipcode)
        reg.save()
        messages.success(request,"Congratulations! the profile has been successfully saved")

     else:
        messages.warning(request,"Invalid Inputs")
     return render(request,"templates/profile.html",locals())
   
def address(request):
   add = Customer.objects.filter(user=request.user)
   return render(request,"templates/address.html",locals())

class updateAddress(View):
   def get(self,request,pk):
      add = Customer.objects.get(pk=pk)
      form = CustomerProfileForm(isinstance=add)
      return render(request,"templates/updateAddress.html",locals())

   def post(self,request,pk):
      form = CustomerProfileForm(request.POST)
      if form.is_valid():
         add = Customer.objects.get(pk=pk)
         add.name = form.cleaned_data['name']
         add.locality = form.cleaned_data['locality']
         add.city = form.cleaned_data['city']
         add.mobile = form.cleaned_data['mobile']
         add.state = form.cleaned_data['state']
         add.zipcode= form.cleaned_data['zipcode']
         add.save()
         messages.success(request,"Congratulations! Profile data has been updated successfully")
      else:
         messages.warning(request,"Invalid Data")
      return redirect("address")
   
def ad_to_cart(request):
   pass

  

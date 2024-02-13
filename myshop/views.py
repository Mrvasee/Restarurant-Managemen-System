from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Southindian,Chinese,CartItem,Signup_model,Book_Table
from django.template import loader
from django.contrib import messages
import random
import string
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
# Create your views here.

# rendring the Home Page
def Home(request):
    return render(request,'home.html') 

#rendering the Menu Page
def Menu(request):
    chinese_dishes=Chinese.objects.all()  # Retrive Chinese Dishes from the Database
    southindian_dishes=Southindian.objects.all()  # Retrive southindian Dishes from the Database
    context={ 'Data': chinese_dishes ,'Dishes':southindian_dishes,'cuisine_s':'Southindian','cuisine_c':'Chinese'}
    return render(request,"menu.html",context)

#Book a Table    
def Book_table(request):
    if request.method=="POST":
        name=request.POST.get('name')      
        email=request.POST.get('email')   
        phone=request.POST.get('phone')    
        date=request.POST.get('date')      
        time=request.POST.get('time')     
        people=request.POST.get('people')  
        msg=request.POST.get('message') 
        if not (name and email and phone and date and time and people):
            # If any required field is missing, render the form with an error message
            return render(request, 'home.html', {'error_message': 'Please fill out all required fields'})
   
        book_a_table=Book_Table(Name=name ,Email= email,Phone_No=phone ,Date= date,Time=time ,People=people ,Message=msg)    
        book_a_table.save()     # Save all the data into the Database
    
    # createing OTP for verification 
        return render(request, 'home.html', {'success_message': 'Your booking request was sent. We will call back or send an Email to confirm your reservation. Thank you!'})

    return render(request,'home.html')

# Registering user
def  Signup(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname =request.POST.get('lname')
        email=request.POST.get('email')
        pno=request.POST.get('pno')
        address=request.POST.get('address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        zipcode=request.POST.get('zipcode')
        signup=Signup_model(First_name=fname,Last_name=lname,Email=email,Phone_No=pno,Address=address,City=city,State=state,Pincode=zipcode)
        signup.save()
        messages.success(request, "Account Created successfully")
        return render(request,'signup.html')
    return render(request,'signup.html')

#  when Searching a dishes in the Search bar this  function called
def Search(request):
    if request.method=='GET':
        query=request.GET.get('query')
        chinese_data = Chinese.objects.filter(Name__icontains=query)  # Match the Query in Chinese Dastabase
        southindian_data = Southindian.objects.filter(Name__icontains=query)  #Match the Query in Southindian Dastabase
        data = list(chinese_data) + list(southindian_data)
        if not data:
            messages=' Sorry , This Dish is Not Available'
            chinese_dishes=Chinese.objects.all()  # Retrive Chinese Dishes from the Database
            southindian_dishes=Southindian.objects.all()  # southindian Dishes from the Database
            context={ 'Data': chinese_dishes ,'Dishes':southindian_dishes,'message':messages,'cuisine_s':'Southindian','cuisine_c':'Chinese'}
            return render(request,"menu.html",context)
        context = {
        'Data': data,
         }
        return render(request,'menu.html',context)
    chinese_dishes=Chinese.objects.all()  # Retrive Chinese Dishes from the Database
    southindian_dishes=Southindian.objects.all()  # Retrive southindian Dishes from the Database
    context={ 'Data': chinese_dishes ,'Dishes':southindian_dishes}
    return render(request,"menu.html",context)

# When User Entered Valid OTP then, this Function is called
def Login(request):
    if request.method=='POST':
        otp=request.POST.get('otp')
        stored_otp=request.session.get('otp')
        if otp== stored_otp:
            del request.session['otp']
            return render(request, 'otp_validate.html', {'otp_matched': True})
    
    return render(request, 'otp_validate.html', {'otp_matched': False})

# Send OTP through Gmail
def Send_otp(request):
    if request.method=='POST':      
        try:
            email=request.POST.get('email')
            signup=Signup_model.objects.get(Email=email)
            characters = string.digits
            otp = ''.join(random.choice(characters) for _ in range(6))
            request.session['otp']=otp
            subject = 'Your OTP for Login'
            message = f'Your OTP is: {otp}'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)
            messages.success(request,f"OTP has been sent to {email}")
            return render(request,'otp_validate.html')
        except Signup_model.DoesNotExist:
            messages.error(request,'Email Does Not Exists')
            return render(request,'login.html')            
    return render(request,'login.html')


# Add The Dish to The Cart
def Add_to_cart(request, product_id,dish_type):
    if dish_type=='Chinese':
        product = Chinese.objects.get(id=product_id)
        cart_item, created = CartItem.objects.get_or_create(chinese=product)
    elif dish_type=='Southindian':
        product = Southindian.objects.get(id=product_id)
        cart_item, created =CartItem.objects.get_or_create(southindian=product)        
    else:
        chinese_dishes=Chinese.objects.all()  # Retrive Chinese Dishes from the Database
        southindian_dishes=Southindian.objects.all()  # Retrive southindian Dishes from the Database
        context={ 'Data': chinese_dishes ,'Dishes':southindian_dishes,'cuisine_s':'Southindian','cuisine_c':'Chinese'}
        return render(request,"menu.html",context)                                                     
    cart_item.quantity += 1
    cart_item.save()
    return redirect('myshop:menu')

# rendering to the View Cart Page
def View_cart(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.chinese.Price * item.quantity if item.chinese else item.southindian.Price * item.quantity for item in cart_items)
    context={'cart_items': cart_items, 'total_price': total_price}
    return render(request, 'view_cart.html',context )

# Remove the Dosh from the Cart
def Remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('myshop:view-cart')
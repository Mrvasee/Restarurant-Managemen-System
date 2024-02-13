from django.urls import path
from . import views
app_name = 'myshop'
urlpatterns=[

    path('home',views.Home,name='home'),
    path('Menus',views.Menu,name='menu'),
    path('Book-Table',views.Book_table,name='book-table'),
    
    path('login',views.Login,name='login'),
    path('signup',views.Signup,name='signup'),
    path('cart/<int:product_id>/<str:dish_type>',views.Add_to_cart,name='cart-details'),
    path('viewcart',views.View_cart,name='view-cart'),
    path('remove/<int:item_id>',views.Remove_from_cart,name='remove-cart'),
    path('mail',views.Send_otp,name='otp'),
    path('search',views.Search,name='search'),
]
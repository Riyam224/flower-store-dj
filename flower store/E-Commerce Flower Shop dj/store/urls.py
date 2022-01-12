from django.urls import path 
from . import views 



urlpatterns = [
    path('' , views.home, name='home'),
    path('<int:id>/' , views.flower_details , name='flower_details'),
    
    path('<int:id>/flower_fav/' , views.flower_fav , name='flower_fav'),
    path('flower_fav_list/', views.flower_fav_list , name='flower_fav_list'),
    

    path('share/' , views.share , name='share'),


    # add to cart and chaekcout 
   
    path('cart/' , views.add_to_cart , name='cart'),
    path('checkout/' , views.checkout , name='checkout'),

    path('add_to_cart/<slug>/' , views.add_to_cart , name='add_to_cart'),
    

]

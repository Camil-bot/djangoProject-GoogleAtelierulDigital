"""TravelApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from TravelYourself.views import homepage, Cart, register,homepage, add2cart, ListCart
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('django.contrib.auth.urls'), {'next_page': '/'}, name='login'),
    path('login/', LoginView.as_view(template_name='login.html'), {'next_page': 'homepage'},  name='login'),
    path('homepage/', homepage.as_view(), name='vaykay'),
    path('', register, name='register'),
    path('cart/', ListCart.as_view(), {'next_page': 'cart.html'}, name='cart')
    # path('cart/<int:pk>', add2cart, name="add2cart"),


    # path('cart/', CreateCart.as_view(), {'next_page': 'homepage.html'}, name='add_2_cart')

    # path('homepage/', views.UpdateCart.as_view(), name='update-cart'),

]



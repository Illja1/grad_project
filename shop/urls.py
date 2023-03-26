from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import GeeksDetailView
urlpatterns = [
    path('',views.nav,name='nav'),
    path('category/<str:category_name>/', views.furniture_by_category, name='category'),
    path('login',views.user_login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.user_logout,name= 'logout'),
    path('add',views.create_furniture,name='add'),
    path('add_c',views.create_category,name='add_c'),
    path('cart',views.cart,name='cart'),
    path('checkout',views.checkout,name='checkout'),
    path('update_item/',views.upadateItem,name='upadate'),
    path('process_order/',views.processOrder,name='process_order'),
    path('<int:pk>', GeeksDetailView.as_view(),name='detail'),
    path('chatbot/', views.ChatbotView.as_view(), name='chatbot'),
    ]



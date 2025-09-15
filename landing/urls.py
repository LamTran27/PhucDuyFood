from django.urls import path
from . import views
from .views import footer_signup

urlpatterns = [
    path('', views.product_intro, name='product_intro'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('footer-signup/', footer_signup, name='footer_signup'),
]

from django.urls import path, include

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.landingPage, name='landingPage'),
    path('register/', views.registerPage, name='registerPage'),
    path('email-verification/', views.emailVerification, name='emailVerification'),  
    path('email-verification/<str:name>', views.confirmedEmail, name='confirmedEmail'),  
    path('product/<str:search>', views.productPage, name='productPage'),
    path('product/', views.productPageAll, name='productPageAll'),
    path('detail-product/<str:id>', views.detailproduct, name='detailproduct')
]
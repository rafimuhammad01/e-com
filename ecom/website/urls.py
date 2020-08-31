from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('register/', views.registerPage, name='registerPage'),
    path('email-verification/', views.emailVerification, name='emailVerification'),  
    path('email-verification/<str:name>', views.confirmedEmail, name='confirmedEmail')
]
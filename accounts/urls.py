from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='dashboard'),
    path('forgetPassword', views.forgetPassword, name='forgetPassword'),
    path('resetPassword', views.resetPassword, name='resetPassword'),

    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('resetpassword_validate/<uidb64>/<token>', views.resetpassword_validate, name='resetpassword_validate')
] 
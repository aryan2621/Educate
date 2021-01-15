from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('achievements',views.achievements,name='achievements'),
    path('teacher_intro',views.teacher_intro,name='teacher_intro'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),

    

    




]

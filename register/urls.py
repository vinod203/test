from django.urls import path
from . import views
from .views import StudentUpdateView
from register.views import home, stud_register, stud_all, stud_delete,stud_search
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home,name='home'),
    path('stud-reg/',stud_register,name='Student-Registration'),
    # path('stud-reg/',StudentRegister.as_view(),name='Student-Registration'),
    path('stud-update/<int:pk>/',StudentUpdateView.as_view(),name='student-update'),
    path('stud-delete/',stud_delete,name='Student-deletion'),
    path('stud-all/',stud_all,name='Students-list'),
    path('stud-list/', views.StudentCRUDView.as_view(), name='Students-list'),
    path('stud-search/',stud_search,name='Students-search'),
    path('login/',auth_views.LoginView.as_view(template_name='register/login.html'),name='login'),
    path('logout/',auth_views.LoginView.as_view(template_name='register/logout.html'),name='logout'),
    path('profile/',views.profile,name='profile'),
    path('register/',views.register,name='register'),
    path('data/',views.StudentListView.as_view())

]

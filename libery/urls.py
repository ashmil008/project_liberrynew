"""
URL configuration for libery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import django.core.mail.backends.console
from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.display,name="home"),
    path('register',views.register),
    path('Login',views.log,name="Login"),
    path('lib',views.liberain,name="lib"),
    path('add',views.addbook),
    path('update/<int:id>',views.edit_book, name='update'),
    path('details/<int:id>/',views.book_details, name='details'),
    path('profile',views.profile,name="profile"),
    path('logout/',views.logout_view,name="logout"),
    path('delete-book/<int:id>/', views.delete_book, name="delete-book"),
    path('search/',views.search_book,name="search"),
    path('editprofileLib/<int:id>/',views.edit_profileLib, name="editprofile"),
    path('edituserprofile/<int:id>/',views.edituserprofile, name="edit-user"),
    path('passwordpro/<int:id>/',views.chnage_passwordpro, name="password"),
    path('passwordlib/<int:id>/',views.chnage_passwordlib, name="passwordlib"),
    path('borrow_book/<int:id>/',views.borrow_book, name="borrow_book"),
    path('history_lib',views.historylib, name="history_lib"),
    path('history_pro',views.historyuser, name="history"),
    path('return/<int:id>',views.return_book, name="return"),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

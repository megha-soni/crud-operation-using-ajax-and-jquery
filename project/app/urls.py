from django.urls import path
from app import views

urlpatterns=[
    path('',views.Home,name='home'),
    path('savedata/',views.SaveData,name='savedata'),
    path('deletedata/',views.DeleteData,name='deletedata'),
    path('editdata/',views.EditData,name='editdata'),
]
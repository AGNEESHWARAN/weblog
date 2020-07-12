from django.urls import path
from blog import views
app_name='blog'
urlpatterns=[
path('index/',views.index,name='blogindex'),
path('desk/',views.desk,name='desk'),
path('login/',views.login,name='login'),
path('logout/',views.logout,name='logout'),
path('signup/',views.signup,name='signup'),
path('addblog/',views.addblog,name='addblog'),

]

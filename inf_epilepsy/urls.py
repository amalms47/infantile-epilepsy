from django.urls import path
from inf_epilepsy import views

urlpatterns = [

    path('' , views.index , name='index'),
    path('dashboard/' , views.dashboard, name='dashboard'),
    path('baselinedata/', views.baselinedata, name='baselinedata'),
    path('logout/' , views.logout_user,name='logout'),
    path('page_404/', views.error_404, name='page_404'),
]

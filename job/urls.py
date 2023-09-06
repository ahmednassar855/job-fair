from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.job_lists),
    path('<int:id>', views.job_detial),
]

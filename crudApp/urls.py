from django.urls import path
from . import views

urlpatterns = [
    path('check/', views.retrieve_view),
    path('create/', views.create_view),
    path('delete/<id>', views.delete_view),
    path('update/<id>', views.update_view)
]

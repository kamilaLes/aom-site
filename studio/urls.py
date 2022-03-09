from django.urls import path
from . import views

urlpatterns = [
    path("",views.Index.as_view(), name="index"),
    path("classes", views.ClassesView.as_view(), name="classes"),
    path("classes/<slug:slug>", views.SingleClassesView.as_view(), name="classes-detail"),
    path("trainers", views.TrainersView.as_view(), name="trainers"),
    path("trainers/<int:pk>", views.TrainerDetails.as_view(),name="trainer-detail"),
    path("client-form", views.FormView.as_view(), name="client-form"),
    path("thank-you",views.ThankYouView.as_view(), name='thank-you')
]
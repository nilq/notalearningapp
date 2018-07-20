from django.urls import path, include
from .           import views

from django.views.generic import TemplateView

urlpatterns = [
    path('',       TemplateView.as_view(template_name="rango/index.html"), name='index'),
    path('about/', views.about, name='about'),
]
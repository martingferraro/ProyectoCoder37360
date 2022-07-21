from django.urls import path
from .views import *


urlpatterns = [
    path('cursos/', cursos),
    path('curso/', curso),
    path('profesores/', profesores),
    path('estudiantes/', estudiantes),
    path('entregables/', entregables),
    path('', inicio),

]

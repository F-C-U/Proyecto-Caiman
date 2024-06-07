from django.urls import include, path
from .views import registrouser
urlpatterns = [
    path('registrouser', registrouser, name='registrouser'),
]

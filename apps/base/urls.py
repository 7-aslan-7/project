from django.urls import path
from apps.base.views import index_1

urlpatterns = [
    path('', index_1, name="index"),
]

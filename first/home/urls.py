from django.urls import path
from home.views import UniversityListView

urlpatterns = [
    path('universities/', UniversityListView.as_view(), name='university_list'),
]
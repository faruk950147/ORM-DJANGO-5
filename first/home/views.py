from django.views import View
from django.shortcuts import render
from .models import University, Department


class HomeView(View):
    def get(self, request):
        universities = University.objects.all()
        departments = Department.objects.all()
        return render(request, 'home/home.html', {'universities': universities, 'departments': departments})

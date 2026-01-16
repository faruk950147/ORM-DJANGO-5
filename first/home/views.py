from django.shortcuts import render
from django.views import View

from home.models import University, Department
# Create your views here.

class UniversityListView(View):
    def get(self, request):
        universities = University.objects.all()
        return render(request, 'home/home.html', {'universities': universities})
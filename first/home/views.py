from django.views import View
from django.shortcuts import render
from home.models import University, Department
from django.db import connection

class HomeView(View):
    def get(self, request):
        universities = University.objects.all()
        departments = Department.objects.all()

        # Force query execution
        list(universities)
        list(departments)

        # Print raw SQL queries
        # print('Universities SQL:', universities.query)
        # print('Departments SQL:', departments.query)
        print('Database Queries Executed:', connection.queries)

        return render(request, 'home/home.html', {
            'universities': universities,
            'departments': departments
        })
class AboutView(View):
    def get(self, request):
        return render(request, 'home/about.html')
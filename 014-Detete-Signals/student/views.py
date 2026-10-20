
from django.shortcuts import render
from .models import Student
from django.db import connection
from django.db.models import Q


# Part 2
#################################################################

################
# Example 1: All Students
################

# def student_list_(request):
#
#     posts = Student.objects.all()
#
#     print(posts)
#     print(posts.query)
#     print(connection.queries)
#
#     return render(request, 'output.html', {'posts': posts})


################
# Example 2: Simple OR using |
################

# def student_list_(request):
#
#     posts = Student.objects.filter(
#         surname__startswith='austin'
#     ) | Student.objects.filter(
#         surname__startswith='baldwin'
#     )
#
#     print(posts)
#     print(posts.query)
#     print(connection.queries)
#
#     return render(request, 'output.html', {'posts': posts})


################
# Example 3: OR using Q and NOT using ~
################

def student_list(request):

    posts = Student.objects.filter(
        Q(surname__startswith='austin') |
        ~Q(surname__startswith='baldwin') |
        Q(surname__startswith='avery-parker')
    )

    print(posts)
    print(posts.query)
    print(connection.queries)

    return render(request, 'output.html', {'posts': posts})

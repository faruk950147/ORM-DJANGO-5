
from django.shortcuts import render
from .models import Student, Teacher
from django.db import connection
from django.db.models import Q


# Part 2
#################################################################

# Example 1: All Students

# def student_list_(request):
#
#     posts = Student.objects.all()
#
#     print(posts)
#     print(posts.query)
#     print(connection.queries)
#
#     return render(request, 'output.html', {'posts': posts})


# Example 2: OR Operator

# def student_list_(request):
#
#     posts = (
#         Student.objects.filter(surname__startswith='austin')
#         | Student.objects.filter(surname__startswith='baldwin')
#     )
#
#     print(posts)
#     print(posts.query)
#     print(connection.queries)
#
#     return render(request, 'output.html', {'posts': posts})


# Example 3: Q Object with OR and NOT

# def student_list_(request):
#
#     posts = Student.objects.filter(
#         Q(surname__startswith='austin')
#         | ~Q(surname__startswith='baldwin')
#         | Q(surname__startswith='avery-parker')
#     )
#
#     print(posts)
#     print(posts.query)
#     print(connection.queries)
#
#     return render(request, 'output.html', {'posts': posts})


# Part 3
#################################################################

# Example 4: AND Operator using &

# def student_list_(request):
#
#     posts = (
#         Student.objects.filter(classroom=1)
#         & Student.objects.filter(age=20)
#     )
#
#     print(posts)
#     print(posts.query)
#     print(connection.queries)
#
#     return render(request, 'output.html', {'posts': posts})


# Example 5: AND Operator using Q()

# def student_list_(request):
#
#     posts = Student.objects.filter(
#         Q(surname__startswith='baldwin')
#         & Q(firstname__startswith='lakisha')
#     )
#
#     print(posts)
#     print(posts.query)
#     print(connection.queries)
#
#     return render(request, 'output.html', {'posts': posts})


# Part 4
#################################################################

# UNION: Student and Teacher firstname

def student_list(request):

    posts = (
        Student.objects.all()
        .values_list('firstname')
        .union(
            Teacher.objects.all().values_list('firstname')
        )
    )

    print(posts)
    print(posts.query)
    print(connection.queries)

    return render(request, 'output.html', {'posts': posts})


from django.shortcuts import render
from .models import Student, Teacher
from django.db import connection
from django.db.models import Q


# Part 2
#################################################################

################
# Simple OR
################

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


# Example 2: OR using |

# def student_list_(request):
#
#     posts = Student.objects.filter(
#         surname__startswith='austin'
#     ) | Student.objects.filter(
#         surname__startswith='baldwin'
#     )
#
#     print(posts)
#     print(connection.queries)
#
#     return render(request, 'output.html', {'posts': posts})


# Example 3: OR using Q and NOT using ~

# def student_list_(request):
#
#     posts = Student.objects.filter(
#         Q(surname__startswith='austin') |
#         ~Q(surname__startswith='baldwin') |
#         Q(surname__startswith='avery-parker')
#     )
#
#     print(posts)
#     print(connection.queries)
#
#     return render(request, 'output.html', {'posts': posts})


# Part 3
#################################################################

################
# Simple AND
################

# Example 1: AND using &

# def student_list_(request):
#
#     posts = Student.objects.filter(
#         classroom=1
#     ) & Student.objects.filter(
#         age=20
#     )
#
#     print(posts)
#     print(connection.queries)
#
#     return render(request, 'output.html', {'posts': posts})


# Example 2: AND using Q

# def student_list_(request):
#
#     posts = Student.objects.filter(
#         Q(surname__startswith='baldwin') &
#         Q(firstname__startswith='lakisha')
#     )
#
#     print(posts)
#     print(connection.queries)
#
#     return render(request, 'output.html', {'posts': posts})


# Part 4
#################################################################

################
# Simple UNION
################

# def student_list_(request):
#
#     posts = Student.objects.all().values_list(
#         'firstname'
#     ).union(
#         Teacher.objects.all().values_list('firstname')
#     )
#
#     print(posts)
#     print(connection.queries)
#
#     return render(request, 'output.html', {'posts': posts})


# Part 5
#################################################################

################
# Simple EXCLUDE
################

# Example 1: Exclude students older than 19

# def student_list_(request):
#
#     posts = Student.objects.exclude(age__gt=19)
#
#     # gt  = Greater than
#     # gte = Greater than or equal to
#     # lt  = Less than
#     # lte = Less than or equal to
#
#     print(posts)
#     print(connection.queries)
#
#     return render(request, 'output.html', {'posts': posts})


# Example 2: NOT using Q

# def student_list_(request):
#
#     posts = Student.objects.filter(
#         ~Q(age__gt=20) &
#         ~Q(surname__startswith='baldwin')
#     )
#
#     print(posts)
#     print(connection.queries)
#
#     return render(request, 'output.html', {'posts': posts})


# Part 6
#################################################################

################
# SELECT & OUTPUT INDIVIDUAL FIELDS
################

# def student_list_(request):
#
#     posts = Student.objects.filter(
#         classroom=1
#     ).only('firstname', 'age')
#
#     print(posts)
#     print(connection.queries)
#
#     return render(request, 'output.html', {'data': posts})


# Part 7
#################################################################

################
# Simple PERFORMING RAW QUERIES
################



from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from .models import Student


# CREATE
def student_create(request):

    if request.method == 'POST':

        firstname = request.POST.get('firstname')
        surname = request.POST.get('surname')
        age = request.POST.get('age')
        classroom = request.POST.get('classroom')

        sql = """
            INSERT INTO student_student
            (firstname, surname, age, classroom)
            VALUES (%s, %s, %s, %s)
        """

        with connection.cursor() as cursor:
            cursor.execute(
                sql,
                [firstname, surname, age, classroom]
            )

        return redirect('student_list')

    return render(request, 'create.html')


# READ ALL
def student_list(request):

    sql = "SELECT * FROM student_student"

    posts = Student.objects.raw(sql)

    print(posts)
    print(connection.queries)

    return render(request, 'output.html', {'data': posts})


# READ SINGLE
def detail(request, id):

    sql = "SELECT * FROM student_student WHERE id = %s"

    student = list(Student.objects.raw(sql, [id]))

    if not student:
        return HttpResponse("Student not found", status=404)

    return render(
        request,
        'detail.html',
        {'student': student[0]}
    )


# UPDATE
def student_update(request, id):

    sql = "SELECT * FROM student_student WHERE id = %s"

    student = list(Student.objects.raw(sql, [id]))

    if not student:
        return HttpResponse("Student not found", status=404)

    student = student[0]

    if request.method == 'POST':

        firstname = request.POST.get('firstname')
        surname = request.POST.get('surname')
        age = request.POST.get('age')
        classroom = request.POST.get('classroom')

        sql = """
            UPDATE student_student
            SET firstname = %s,
                surname = %s,
                age = %s,
                classroom = %s
            WHERE id = %s
        """

        with connection.cursor() as cursor:
            cursor.execute(
                sql,
                [firstname, surname, age, classroom, id]
            )

        return redirect('student_list')

    return render(
        request,
        'update.html',
        {'student': student}
    )


# DELETE
def student_delete(request, id):

    if request.method == 'POST':

        sql = "DELETE FROM student_student WHERE id = %s"

        with connection.cursor() as cursor:
            cursor.execute(sql, [id])

        return redirect('student_list')

    return HttpResponse(
        "Use POST request to delete a student.",
        status=405
    )

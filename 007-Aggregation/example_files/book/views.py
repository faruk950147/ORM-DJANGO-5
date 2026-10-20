
from django.db.models import Sum, Max, Min, Avg
from book.models import Book
from django.views.generic import ListView


# Function-based view example
# def example(request):
#     data = Book.objects.aggregate(
#         sum=Sum('ratings_count'),
#         max=Max('ratings_count'),
#         min=Min('ratings_count'),
#         avg=Avg('ratings_count')
#     )
#
#     return render(request, 'index.html', {'data': data})


# Class-based view using ListView
class Example(ListView):

    model = Book
    template_name = 'index.html'
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['ratings_count'] = Book.objects.aggregate(
            sum=Sum('ratings_count'),
            max=Max('ratings_count'),
            min=Min('ratings_count'),
            avg=Avg('ratings_count')
        )

        return context


from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from store.models import Product

from .basket import Basket


def basket_summary(request):
    basket = Basket(request)
    return render(request, 'basket/summary.html', {'basket': basket})


def basket_add(request):
    basket = Basket(request)

    if request.method == 'POST' and request.POST.get('action') == 'post':
        try:
            product_id = int(request.POST.get('productid'))
            product_qty = int(request.POST.get('productqty'))

            if product_qty <= 0:
                return JsonResponse({'error': 'Quantity must be greater than zero.'}, status=400)

            product = get_object_or_404(Product, id=product_id)
            basket.add(product=product, qty=product_qty)

            basketqty = basket.__len__()
            response = JsonResponse({'qty': basketqty})
            return response

        except (TypeError, ValueError):
            return JsonResponse({'error': 'Invalid product ID or quantity.'}, status=400)

    return JsonResponse({'error': 'Invalid request.'}, status=400)


def basket_delete(request):
    basket = Basket(request)

    if request.method == 'POST' and request.POST.get('action') == 'post':
        try:
            product_id = int(request.POST.get('productid'))

            basket.delete(product=product_id)

            basketqty = basket.__len__()
            baskettotal = basket.get_total_price()

            response = JsonResponse({
                'qty': basketqty,
                'subtotal': baskettotal
            })
            return response

        except (TypeError, ValueError):
            return JsonResponse({'error': 'Invalid product ID.'}, status=400)

    return JsonResponse({'error': 'Invalid request.'}, status=400)


def basket_update(request):
    basket = Basket(request)

    if request.method == 'POST' and request.POST.get('action') == 'post':
        try:
            product_id = int(request.POST.get('productid'))
            product_qty = int(request.POST.get('productqty'))

            if product_qty <= 0:
                return JsonResponse({'error': 'Quantity must be greater than zero.'}, status=400)

            basket.update(product=product_id, qty=product_qty)

            basketqty = basket.__len__()
            basketsubtotal = basket.get_subtotal_price()

            response = JsonResponse({
                'qty': basketqty,
                'subtotal': basketsubtotal
            })
            return response

        except (TypeError, ValueError):
            return JsonResponse({'error': 'Invalid product ID or quantity.'}, status=400)

    return JsonResponse({'error': 'Invalid request.'}, status=400)

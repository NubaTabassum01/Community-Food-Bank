from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Family, FoodStock, Distribution


def home(request):
    families = Family.objects.all()
    stock = FoodStock.objects.first()

    if stock is None:
        stock = FoodStock.objects.create(quantity=0)

    history = Distribution.objects.all().order_by('-date')

    if request.method == 'POST':
        action = request.POST.get('action')

        try:
            if action == 'register':
                name = request.POST.get('name', '').strip()
                members = int(request.POST.get('members', 0))

                if not name or members <= 0:
                    messages.error(request, 'Enter valid family details.')
                else:
                    Family.objects.create(
                        name=name,
                        member_count=members
                    )
                    messages.success(request, 'Family registered!')

            elif action == 'add_stock':
                quantity = int(request.POST.get('quantity', 0))

                if quantity <= 0:
                    messages.error(request, 'Quantity must be positive.')
                else:
                    stock.quantity += quantity
                    stock.save()
                    messages.success(request, 'Food stock added!')

            elif action == 'distribute':
                family_id = int(request.POST.get('family_id', 0))
                quantity = int(request.POST.get('quantity', 0))
                family = Family.objects.filter(id=family_id).first()

                if family is None or quantity <= 0:
                    messages.error(request, 'Invalid family or quantity.')
                elif quantity > stock.quantity:
                    messages.error(request, 'Not enough food stock.')
                else:
                    stock.quantity -= quantity
                    stock.save()

                    Distribution.objects.create(
                        family=family,
                        quantity=quantity
                    )
                    messages.success(request, 'Food distributed!')

        except (ValueError, TypeError):
            messages.error(request, 'Please enter valid numbers.')

        return redirect('home')

    total_distributed = sum(item.quantity for item in history)

    return render(request, 'home.html', {
        'families': families,
        'stock': stock,
        'history': history,
        'total_distributed': total_distributed,
    })
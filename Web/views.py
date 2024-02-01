from django.http import JsonResponse
from django.shortcuts import render
from django_countries import countries
from .models import *
from .forms import *
from .filters import *

BOOKING_AMOUNT_PERCENTAGE = 0.20

def home(request, country_code='ae'):
    group_tours = GroupTour.objects.filter(from_country=country_code.upper())
    context = { 'group_tours': group_tours, 'country_code': country_code }

    return render(request, f'{country_code}/home.html', context)

def group_tours(request, country_code='ae'):
    group_tours = GroupTour.objects.filter(from_country=country_code.upper())
    filter = GroupTourFilter(request.GET, queryset=group_tours)
    group_tours = filter.qs
    context = { 'country_code': country_code, 'group_tours': group_tours, 'filter': filter, }

    return render(request, f'{country_code}/group_tour/index.html', context)

def view_group_tour_default(request, group_tour_id):
    country_code = 'ae'
    group_tour = GroupTour.objects.get(id=group_tour_id, from_country=country_code.upper())
    packages = group_tour.package_set.all()
    add_ons = group_tour.addon_set.all()
    price = packages.first().price
    form = BookingForm(initial={'group_tour': group_tour}, packages=packages, add_ons=add_ons)
    customer_form = CustomerForm()

    if request.method == 'POST':
        form = BookingForm(request.POST, initial={'group_tour': group_tour}, packages=packages, add_ons=add_ons)
        customer_form = CustomerForm(request.POST)

        if form.is_valid() and customer_form.is_valid():
            selected_package = form.cleaned_data['package']
            selected_add_on = form.cleaned_data['add_on']
            add_on_quantity = selected_package.people
            total_amount = selected_package.price + (selected_add_on.price * add_on_quantity)
            booking_amount = BOOKING_AMOUNT_PERCENTAGE * total_amount

            customer = customer_form.save()

            booking = form.save(commit=False)
            booking.group_tour = group_tour
            booking.total_amount = total_amount
            booking.booking_amount = booking_amount
            booking.customer = customer
            booking.save()
        else:
            print(form.errors)

    context = {
        'country_code': country_code,
        'group_tour': group_tour,
        'price': price,
        'form': form,
        'customer_form': customer_form,
    }

    return render(request, f'{country_code}/group_tour/view.html', context)

def view_group_tour_region(request, country_code, group_tour_id):
    group_tour = GroupTour.objects.get(id=group_tour_id, from_country=country_code.upper())
    packages = group_tour.package_set.all()
    add_ons = group_tour.addon_set.all()
    price = packages.first().price
    form = BookingForm(initial={'group_tour': group_tour}, packages=packages, add_ons=add_ons)
    customer_form = CustomerForm()

    if request.method == 'POST':
        form = BookingForm(request.POST, initial={'group_tour': group_tour}, packages=packages, add_ons=add_ons)
        customer_form = CustomerForm(request.POST)

        if form.is_valid() and customer_form.is_valid():
            selected_package = form.cleaned_data['package']
            selected_add_on = form.cleaned_data['add_on']
            add_on_quantity = selected_package.people
            total_amount = selected_package.price + (selected_add_on.price * add_on_quantity)
            booking_amount = BOOKING_AMOUNT_PERCENTAGE * total_amount

            customer = customer_form.save()

            booking = form.save(commit=False)
            booking.group_tour = group_tour
            booking.total_amount = total_amount
            booking.booking_amount = booking_amount
            booking.customer = customer
            booking.save()
        else:
            print(form.errors)


    context = {
        'country_code': country_code,
        'group_tour': group_tour,
        'price': price,
        'form': form,
        'customer_form': customer_form,
    }

    return render(request, f'{country_code}/group_tour/view.html', context)

def get_price(request, country_code):
    package_id = request.GET.get('package_id')
    add_on_id = request.GET.get('add_on_id')

    package_price = 0
    add_on_price = 0
    add_on_description = ''

    if package_id:
        package = Package.objects.get(pk=package_id)
        package_price = package.price
        if add_on_id:
            add_on = AddOn.objects.get(pk=add_on_id)
            add_on_price = (add_on.price * package.people)
            add_on_description = add_on.description

    total_price = package_price + add_on_price
    booking_amount = format_currency(country_code, (total_price * 0.20))
    total_price = format_currency(country_code, total_price)

    context = {
        'total_price': total_price,
        'booking_amount': booking_amount,
        'add_on_description': add_on_description,
    }

    return JsonResponse(context)

def format_currency(country_code, amount):
    print(f'CODE: {country_code}')
    currency_symbol = 'AED' if country_code == 'ae' else '₹'
    return currency_symbol + str('{:,.2f}'.format(amount))


def booking_payment(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)
    customer = booking.customer

    context = {
        'booking': booking,
        'customer': customer
    }
    return render(request, 'group_tour/payment.html', context)


def iwa_group_of_companies(request):
    return render(request, 'main/iwa_group_of_companies.html', {})

# Theme
def theme_home(request):
    return render(request, 'theme/home.html', {})

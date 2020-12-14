from django.shortcuts import render
from hw20.forms import TicketForm
from django.http import HttpResponse
import datetime


def book_tickets(request):
    if request.method == "GET":
        context = {'form': TicketForm}
        return render(request, 'book_tickets.html', context)
    elif request.method == "POST":
        form = TicketForm(request.POST)
        if not form.is_valid():
            return HttpResponse('Your input is invalid', status=400)
        data = form.cleaned_data
        if data.get('date') < datetime.date.today():
            return HttpResponse('Invalid date - flight in the past', status=400)
        amount = data.get('amount_of_peoples')
        if amount == 1:
            price = 100
        else:
            price = 100 * 2 * amount
        data['price'] = price
        context = {'form': data}
        return render(request, 'datail_tickets.html', context)

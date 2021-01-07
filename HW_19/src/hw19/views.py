from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def index(request):
    return HttpResponse("Hello!")


def task1(request):
    if request.method == 'GET':
        return render(request, "task1.html")
    elif request.method == 'POST':
        words = [request.POST.get('first'), request.POST.get('second'), request.POST.get('third')]
        max_word = words[0]
        for i in words:
            if len(i) > len(max_word):
                max_word = i
        return HttpResponse(max_word)


def task2(request):
    if request.method == 'GET':
        return render(request, 'task2.html')
    elif request.method == 'POST':
        date = request.POST.get('date')
        date_str = datetime.strptime(date, '%Y-%m-%d')
        if date_str.day == 1 and date_str.month == 1:
            return HttpResponse(f'Happy new year {date_str.year}')
        else:
            return HttpResponse(date)

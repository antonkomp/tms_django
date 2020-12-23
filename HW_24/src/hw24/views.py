from django.shortcuts import render, redirect
from django.conf import settings
from django.template import loader
from django.core.mail import send_mail
from requests import get
from hw24.models import NatureImage
from hw24.forms import PictureForm, SendForm


def home(request):
    form = PictureForm()
    if request.method == 'POST':
        form = PictureForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            width = form_data['width']
            height = form_data['height']
            picture_link = get(f'https://picsum.photos/{width}/{height}').url
            picture_data = dict(link=picture_link, width=width, height=height)
            request.session['picture_data'] = picture_data
            return render(request, 'picture.html', {'picture_link': picture_link})
    elif request.method == 'GET':
        return render(request, 'home_page.html', {'form': form})


def save_picture(request):
    if request.method == 'POST':
        picture_data = request.session['picture_data']
        picture_data['comment'] = request.POST['comment']
        NatureImage.objects.create(**picture_data)
        message_dict = {
            'from_whom': settings.EMAIL_HOST_USER,
            'to_whom': settings.EMAIL_HOST_USER,
            'message': f'Comment: {picture_data["comment"]}',
            'subject': 'Picture from Picsum',
            'picture': f'{picture_data["link"]}',
        }
        context = {'form': SendForm(message_dict)}
        return render(request, 'send_to_mail.html', context)
    else:
        return redirect('home')


def send_email(request):
    if request.method == 'POST':
        form = SendForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            html_message = loader.render_to_string('email.html', {'picture': data.get('picture')})
            send_mail(
                subject=data.get('subject'),
                message=data.get('message'),
                html_message=html_message,
                from_email=data.get('from_whom'),
                recipient_list=[data.get('to_whom')],
                fail_silently=False
            )
    return redirect('home')

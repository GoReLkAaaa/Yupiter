import os
from django.shortcuts import render, redirect
from dotenv import load_dotenv
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse


from .models import Prosthetics, Staff
# Create your views here.

load_dotenv()

def index(request):
    templates = 'mainapp/ru/index.html'
    context = {
        'prosthetics': Prosthetics.objects.all(),
    }
    return render(request, templates, context)


def contact(request):
    if request.method == 'GET':
        templates = 'mainapp/ru/html/contact.html'
        return render(request, templates)

    elif request.method == 'POST':
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        phone = request.POST['phone']
        type_amputation = request.POST['type_amputation']
        description = request.POST['textarea']
        email = 'nikitospogorelyn@gmail.com'

        try:
            subject = 'Новая заявка на консультацию'
            text_message = (
                f"Здравствуйте, меня зовут {first_name} {last_name}\n"
                f"Мой номер телефона: {phone}\n"
                f"Тип ампутации: {type_amputation}\n"
                f"Комментарий: {description}"
            )

            html_message = f"""
            <html>
                <body style="font-family: Arial, sans-serif; color:#333;">
                    <h2 style="color:#4CAF50;">Новая заявка на консультацию</h2>
                    <p><b>Здравствуйте!</b></p>
                    <p style="font-size:16px;">Меня зовут 
                       <span style="font-size:18px; font-weight:bold;">{first_name} {last_name}</span></p>
                    <p style="font-size:16px;">📞 Телефон: 
                       <span style="font-size:18px; color:#007BFF;">{phone}</span></p>
                    <p style="font-size:16px;">🦾 Тип ампутации: 
                       <span style="font-size:18px;">{type_amputation}</span></p>
                    <p style="font-size:16px;">Комментарий:</p>
                    <blockquote style="font-size:15px; background:#f9f9f9; padding:10px; border-left:4px solid #ccc;">
                        {description}
                    </blockquote>
                </body>
            </html>
            """
            mail = EmailMultiAlternatives(subject, text_message, to=[email])
            mail.attach_alternative(html_message, "text/html")
            mail.send()

            return redirect('contact')

        except ValueError:
            return redirect('contact')

    else:
        return HttpResponse(
            'Метод не поддерживается',
            status=405
        )


def about(request):
    templates = 'mainapp/ru/html/about.html'
    context = {
        'staff': Staff.objects.all(),
    }
    return render(request, templates, context)


def products(request):
    templates = 'mainapp/ru/html/products.html'
    context = {
        'products': Prosthetics.objects.all(),
    }
    return render(request, templates, context)


def yupiter_uz(request):
    templates = 'mainapp/uz/index_uz.html'
    context = {
        'prosthetics': Prosthetics.objects.all(),
    }
    return render(request, templates, context)


def contact_uz(request):
    if request.method == 'GET':
        templates = 'mainapp/uz/html_uz/contact.html'
        return render(request, templates)

    elif request.method == 'POST':
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        phone = request.POST['phone']
        type_amputation = request.POST['type_amputation']
        description = request.POST['textarea']
        email = 'nikitospogorelyn@gmail.com'

        try:
            subject = 'Новая заявка на консультацию'
            text_message = (
                f"Здравствуйте, меня зовут {first_name} {last_name}\n"
                f"Мой номер телефона: {phone}\n"
                f"Тип ампутации: {type_amputation}\n"
                f"Комментарий: {description}"
            )

            html_message = f"""
                <html>
                    <body style="font-family: Arial, sans-serif; color:#333;">
                        <h2 style="color:#4CAF50;">Новая заявка на консультацию</h2>
                        <p><b>Здравствуйте!</b></p>
                        <p style="font-size:16px;">Меня зовут 
                           <span style="font-size:18px; font-weight:bold;">{first_name} {last_name}</span></p>
                        <p style="font-size:16px;">📞 Телефон: 
                           <span style="font-size:18px; color:#007BFF;">{phone}</span></p>
                        <p style="font-size:16px;">🦾 Тип ампутации: 
                           <span style="font-size:18px;">{type_amputation}</span></p>
                        <p style="font-size:16px;">Комментарий:</p>
                        <blockquote style="font-size:15px; background:#f9f9f9; padding:10px; border-left:4px solid #ccc;">
                            {description}
                        </blockquote>
                    </body>
                </html>
                """
            mail = EmailMultiAlternatives(subject, text_message, to=[email])
            mail.attach_alternative(html_message, "text/html")
            mail.send()

            return redirect('contact')

        except ValueError:
            return redirect('contact')

    else:
        return HttpResponse(
            'Метод не поддерживается',
            status=405
        )


def about_uz(request):
    templates = 'mainapp/uz/html_uz/about.html'
    context = {
        'staff': Staff.objects.all(),
    }
    return render(request, templates, context)


def products_uz(request):
    templates = 'mainapp/uz/html_uz/products.html'
    context = {
        'products': Prosthetics.objects.all(),
    }
    return render(request, templates, context)
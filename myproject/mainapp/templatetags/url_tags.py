from django import template
from django.urls import reverse


register = template.Library()


@register.simple_tag
def get_russian_url(request):
    current_path = request.path
    url_mapping = {
        '/yupiter/uz/': 'index',
        '/contact/uz/': 'contact',
        '/about/uz/': 'about',
        '/products/uz/': 'products',
    }

    if current_path in url_mapping:
        return reverse(url_mapping[current_path])

    if '/ru/' in current_path or current_path == '/':
        return request.get_full_path()

    return reverse('index')


@register.simple_tag
def get_uzbek_url(request):
    current_path = request.path
    url_mapping = {
        '/': 'yupiter_uz',
        '/contact/ru/': 'contact_uz',
        '/about/ru/': 'about_uz',
        '/products/ru/': 'products_uz',
    }


    if current_path in url_mapping:
        return reverse(url_mapping[current_path])

    if '/uz/' in current_path:
        return request.get_full_path()

    return reverse('yupiter_uz')
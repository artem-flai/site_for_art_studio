from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import *
from .models import *

menu_site = [{'name_list': 'Главная страница', 'name_link': 'home', 'pk': '1'},
             {'name_list': 'О нас', 'name_link': 'about', 'pk': '1'},
             {'name_list': 'Для детей', 'name_link': 'little_mk', 'pk': '3'},
             {'name_list': 'Мастер-классы', 'name_link': 'home', 'pk': '1'},
             {'name_list': 'Для взрослых', 'name_link': 'big_mk', 'pk': '4'},
             {'name_list': 'Галерея', 'name_link': 'gallery', 'pk': '1'},
             {'name_list': 'Прайс-лист', 'name_link': 'price_list', 'pk': '1'},
             {'name_list': 'Сотрудничество', 'name_link': 'partners', 'pk': '1'},
             {'name_list': 'Публичная оферта', 'name_link': 'legal', 'pk': '1'},
             {'name_list': 'Контакты', 'name_link': 'contacts', 'pk': '1'},
             {'name_list': 'Корпоративы', 'name_link': 'corporate', 'pk': '5'},
             {'name_list': 'Наша история', 'name_link': 'stories', 'pk': '1'},
             {'name_list': 'Сертификаты', 'name_link': 'sertificates', 'pk': '1'},
             {'name_list': 'Перенаправление', 'name_link': '/', 'pk': '1'},
             {'name_list': 'Записаться на Мастер-класс', 'name_link': '/', 'pk': '1'},
             ]

price = [{"холст": "20х30 акрил", "цена": "40руб."},
         {"холст": "30х40 акрил", "цена": "60руб."},
         {"холст": "40х40 акрил", "цена": "80руб."},
         {"холст": "40х50 акрил", "цена": "90руб."},
         {"холст": "40х60 акрил", "цена": "110руб."},
         {"холст": "50х50 акрил", "цена": "115руб."},
         {"холст": "50х60 акрил", "цена": "120руб."},
         {"холст": "50х70 акрил", "цена": "140руб."},
         {"холст": "60х80 акрил", "цена": "165руб."},
         {"холст": "70х90 акрил", "цена": "185руб."},
         {"холст": "А3 вино", "цена": "40руб."},
         {"холст": "А4 мороженое", "цена": "15руб."},
         ]


class MasterClassAdults(ListView):
    model = MasterClass
    template_name = 'picture/gallery_vzrosly.html'
    context_object_name = 'mk_v'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu_site
        context['title'] = menu_site[4]['name_list']
        context['head'] = menu_site[4]['name_list']
        context['bot_nav1'] = menu_site[7:10]
        context['bot_nav2'] = menu_site[10:13]
        return context


def home_i(request):
    context = {'menu': menu_site,
               'bot_nav1': menu_site[7:10],
               'bot_nav2': menu_site[10:13],
               'title': menu_site[0]['name_list']}
    return render(request, 'picture/home.html', context=context)


class MasterClassKids(ListView):
    model = MasterClass
    template_name = 'picture/gallery_detski.html'
    context_object_name = 'mk_v'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu_site
        context['title'] = menu_site[2]['name_list']
        context['head'] = menu_site[2]['name_list']
        context['bot_nav1'] = menu_site[7:10]
        context['bot_nav2'] = menu_site[10:13]
        return context


def gallery_picture(request, ip_mk):
    mk_info = MasterClass.objects.filter(pk=ip_mk)
    fotos = Gallery_picture.objects.all()
    context = {'bot_nav1': menu_site[7:10],
               'bot_nav2': menu_site[10:13],
               'menu': menu_site,
               'fotos': fotos,
               'mk_info': mk_info,
               'title': menu_site[5]['name_list'],
               'head': menu_site[5]['name_list']}
    return render(request, 'picture/gallery_picture.html', context=context)


def about(request):
    context = {'bot_nav1': menu_site[7:10],
               'bot_nav2': menu_site[10:13],
               'menu': menu_site,
               'title': menu_site[1]['name_list'],
               'head': menu_site[1]['name_list']}
    return render(request, 'picture/about.html', context=context)


def sertificates(request):
    context = {'bot_nav1': menu_site[7:10],
               'bot_nav2': menu_site[10:13],
               'menu': menu_site,
               'title': menu_site[12]['name_list'],
               'head': menu_site[12]['name_list']}
    return render(request, 'picture/sertificates.html', context=context)


def corporate(request):
    context = {'bot_nav1': menu_site[7:10],
               'bot_nav2': menu_site[10:13],
               'menu': menu_site,
               'title': menu_site[10]['name_list'],
               'head': menu_site[10]['name_list']}
    return render(request, 'picture/corporate.html', context=context)


def contacts(request):
    context = {'bot_nav1': menu_site[7:10],
               'bot_nav2': menu_site[10:13],
               'menu': menu_site[0:7],
               'title': menu_site[9]['name_list'],
               'head': menu_site[9]['name_list']}
    return render(request, 'picture/contacts.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def form_writer(request, ip_mk, ip_pict):
    mk = MasterClass.objects.filter(pk=ip_mk)
    pict = Gallery_picture.objects.filter(pk=ip_pict)
    if request.method == 'POST':
        form = FormWrite(ip_mk, ip_pict, request.POST)
        if form.is_valid():
            form.save()
            return redirect('redirect_s')
    else:
        form = FormWrite(ip_mk, ip_pict)
    context = {'form': form,
               'mk': mk,
               'pict': pict,
               'bot_nav1': menu_site[7:10],
               'bot_nav2': menu_site[10:13],
               'title': menu_site[14]['name_list'],
               'head': menu_site[14]['name_list']}
    return render(request, 'picture/form_writer.html', context=context)


def partners(request):
    context = {'bot_nav1': menu_site[7:10],
               'bot_nav2': menu_site[10:13],
               'menu': menu_site[0:7],
               'title': menu_site[7]['name_list'],
               'head': menu_site[7]['name_list']}
    return render(request, 'picture/partners.html', context=context)


def legal(request):
    context = {'bot_nav1': menu_site[7:10],
               'bot_nav2': menu_site[10:13],
               'menu': menu_site[0:7],
               'title': menu_site[8]['name_list'],
               'head': menu_site[8]['name_list']}
    return render(request, 'picture/legal.html', context=context)


def price_list(request):
    context = {'bot_nav1': menu_site[7:10],
               'bot_nav2': menu_site[10:13],
               'menu': menu_site[0:7],
               'title': menu_site[6]['name_list'],
               'head': menu_site[6]['name_list'],
               'price': price
               }
    return render(request, 'picture/price-list.html', context=context)


def redirect_s(request):
    context = {'bot_nav1': menu_site[7:10],
               'bot_nav2': menu_site[10:13],
               'menu': menu_site[0:7],
               'title': menu_site[13]['name_list'],
               'head': menu_site[13]['name_list'],
               }
    return render(request, 'picture/redirect_s.html', context=context)


def stories(request):
    context = {'bot_nav1': menu_site[7:10],
               'bot_nav2': menu_site[10:13],
               'menu': menu_site[0:7],
               'title': menu_site[11]['name_list'],
               'head': menu_site[11]['name_list'],
               }
    return render(request, 'picture/stories.html', context=context)

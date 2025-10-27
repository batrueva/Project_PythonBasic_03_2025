from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from goods.models import Categories



class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Amigurumi - Главная'
        context['content'] = "Магазин игрушек Amigurumi"
        return context


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Amigurumi - О нас'
        context['content'] = "О нас"
        context['text_on_page'] = "Каждая игрушка сделана с душой и любовью."
        return context
    

# def index(request):

#     context = {
#         'title': 'Amigurumi - Главная',
#         'content': "Магазин мебели Amigurumi",
#     }

#     return render(request, 'main/index.html', context)


# def about(request):
#     context = {
#         'title': 'Amigurumi - О нас',
#         'content': "О нас",
#         'text_on_page': "Текст о том почему этот магазин такой классный, и какой хороший товар."
#     }

#     return render(request, 'main/about.html', context)
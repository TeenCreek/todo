from django.views.generic import TemplateView


class Custom404View(TemplateView):
    template_name = 'core/404.html'


class Custom403View(TemplateView):
    template_name = 'core/403.html'


class Custom500View(TemplateView):
    template_name = 'core/500.html'

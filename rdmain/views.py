import datetime

from django.contrib import messages
from django.db.models import Sum, Count
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView
from django.views.generic.base import View

from .forms import RoadForm, RoadCreatForm
from .models import Road


class RoadInfo(TemplateView):
    """Сводная информация на главной странице"""
    template_name = 'index.html'


def ammort(prd_ammort, bst):  # период амортизации и балансовая стоимость
    """расчет амортизации за месяц"""
    norma_ammort = float("{0:.2f}".format(100 / prd_ammort))
    summa_y = float("{0:.2f}".format((bst * norma_ammort) / 100))
    summa_m = float("{0:.2f}".format(summa_y / 12))
    return summa_m  # амортизация за месяц


class RoadInfoView(View):
    """Сводная информация на главной странице"""

    # def get(self, request, *args, **kwargs):
    @staticmethod
    def get(request):
        info = Road.objects.all().aggregate(Count('nroad', distinct=True), Sum('lroad'), Sum('broad'))
        qs = Road.objects.all().filter(onbal=True)
        d_today = datetime.date.today()
        summ_ost = 0
        for rw in qs:
            am_month = ammort(rw.period, rw.broad)
            summ_ost += rw.oroad - am_month * d_today.month
        info['oroad__sum'] = summ_ost
        info['date__today'] = d_today
        return render(request, 'index.html', context=info)


class RoadListView(ListView):
    """Перечень дорог для просмотра"""
    model = Road
    queryset = Road.objects.all().filter(onbal=True)
    template_name = 'rdmain/road_list.html'
    paginate_by = 10


class RoadDetail(DetailView):
    """Информация о дороге"""

    # model = Road
    # template_name = 'rdmain/road_detail.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Road.objects.all()
        else:
            return Road.objects.none()


class RoadUpdateView(UpdateView):
    """Внесение изменений"""
    model = Road
    form_class = RoadForm
    success_url = reverse_lazy('road-list')

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Road.objects.all()
        else:
            return Road.objects.none()

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request, '{}'.format(form.instance))
        return result


class RoadCreateView(CreateView):
    """Заполнение аттрибутов дороги"""
    model = Road
    form_class = RoadCreatForm
    success_url = reverse_lazy('road-list')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request, '{}'.format(form.instance))
        return result

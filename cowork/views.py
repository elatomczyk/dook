from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import TemplateView
from authtools.views import LoginRequiredMixin
from accounts import const
from django.shortcuts import render_to_response

from . import mixins
from . import models
from . import forms


class DashboardView(mixins.UserMixin, LoginRequiredMixin, TemplateView):
    template_name = 'cowork/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        if self.user.user_type == const.USER_TYPE_COMPANY:
            context['last_locations'] = models.Location.objects.filter(company__user=self.user)[:5]
        return context


class SearchView(TemplateView):
    template_name = 'cowork/search.html'

    def get(self, request, *args, **kwargs):
        return render_to_response('cowork/search.html', context_instance=RequestContext(request))

    def post(self, request):
        search_city = request.POST.get('textfield', False)
        cities = models.Location.objects.filter(city=search_city)
        return render_to_response('cowork/search.html', {'cities': cities, 'search_city': search_city}, context_instance=RequestContext(request))


class RentView(TemplateView):
    template_name = 'cowork/rent.html'

    def get(self, request, pk):
        return render_to_response('cowork/rent.html', context_instance=RequestContext(request))

    def post(self, request, pk):
        city = models.Location.objects.get(id=pk)
        user = request.user
        form = forms.DeskCreationForm(request.POST or None)

        if form.is_valid():
            save_it = form.save(commit=False)
            save_it.owner = user
            save_it.location = city
            save_it.save()
            return HttpResponseRedirect('/')



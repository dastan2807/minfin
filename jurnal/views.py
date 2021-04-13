from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import Jurnal
from .forms import JurnalForm, AutoRegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from main.models import MainPersonUser, Name_job
from django.contrib.auth.models import User
from django.db.models import Q
from .filters import JurnalFilter

class JurnalCreate(LoginRequiredMixin, CreateView):
    template_name = 'jurnal/index.html'
    form_class = JurnalForm
    success_url = reverse_lazy('jurnal')
    a = User.objects.get(username='jurnaladmin')
    jurnal_all = Jurnal.objects.all().order_by('date')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = se 
        lf.request.user
        self.object.name_job = MainPersonUser.objects.get(login=self.request.user).name_job
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs['search_filter'] = JurnalFilter()
        kwargs['jurnal_admin'] = self.a
        kwargs['name_job'] = Name_job.objects.all()
        if self.request.GET:
            kwargs['jurnals'] = JurnalFilter(self.request.GET, queryset=self.jurnal_all).qs
        else:
            kwargs['jurnals'] = self.jurnal_all
        kwargs['jurnal_list'] = Jurnal.objects.filter(author=self.request.user)
        if self.request.user != self.a:
            kwargs['main_person'] = MainPersonUser.objects.get(login=self.request.user)
        return super().get_context_data(**kwargs)



class AutoRegister(LoginView):
    template_name = 'jurnal/login.html'
    form_class = AutoRegisterForm
    success_url = reverse_lazy('jurnal')

    def get_success_url(self):
        return self.success_url
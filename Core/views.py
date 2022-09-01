from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import  get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Issue, Status
from django_user_agents.utils import get_user_agent
from django.views.generic import ListView, UpdateView, CreateView, DetailView
from .models import Status, Module
from Auth.models import User
# Create your views here.


class Index(LoginRequiredMixin, ListView):
    login_url = '/auth/login'
    model = Issue
    paginate = 50
    template_name = 'Core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status'] = Status.objects.all()
        context['module'] = Module.objects.all()
        return context


    def get_queryset(self):
        queryset = self.model.objects.filter(reporter=self.request.user).order_by('-id') | self.model.objects.filter(assignee=self.request.user).order_by('-id')
        if self.request.GET.get('issue_number'):
            queryset= self.model.objects.filter(id=self.request.GET.get('issue_number')).order_by('-id')
        if self.request.GET.get('title'):
            queryset= self.model.objects.filter(title__icontains=self.request.GET.get('title')).order_by('-id')
        if self.request.GET.get('date_from'):
            queryset = self.model.objects.filter(create_date__gte=self.request.GET.get('date_from')).order_by('-id')
        if self.request.GET.get('date_to'):
            queryset = self.model.objects.filter(create_date__lte=self.request.GET.get('date_to')).order_by('-id')
        if self.request.GET.get('module'):
            queryset = self.model.objects.filter(module__in=self.request.GET.get('module'))
        if self.request.GET.get('status'):
            queryset = self.model.objects.filter(status_id__in=self.request.GET.get('status'))


        def issue_weight():
            user_list = []
            queryset = User.objects.all()
            for i in queryset:
                user_list.append(i)

            print(user_list)
        issue_weight()
        return queryset




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

# Create your views here.


class Index(LoginRequiredMixin, ListView):
    login_url = '/auth/login'
    model = Issue
    paginate = 50
    template_name = 'Core/index.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(reporter=self.request.user).order_by('-id')
        if self.request.GET.get('issue_number'):
            queryset= self.model.objects.filter(id=self.request.GET.get('issue_number')).order_by('-id')
        if self.request.GET.get('title'):
            queryset= self.model.objects.filter(title__icontains=self.request.GET.get('title')).order_by('-id')
        if self.request.GET.get('date_from'):
            queryset = self.model.objects.filter(create_date__gte=self.request.GET.get('date_from')).order_by('-id')
        if self.request.GET.get('date_to'):
            queryset = self.model.objects.filter(create_date__lte=self.request.GET.get('date_to')).order_by('-id')
        return queryset

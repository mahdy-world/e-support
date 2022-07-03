from django.shortcuts import render
from ONSite.models import *
from django.views.generic import *
from django.contrib.auth.mixins import  LoginRequiredMixin
from .forms import *
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import FormView
import datetime
from django.contrib import messages
from django.http import HttpResponseRedirect



class MyIssue(LoginRequiredMixin, ListView):
    login_url = '/auth/login'
    model = Issue
    paginate = 50

    def get_queryset(self, request):
        queryset = self.model.objects.filter(user=request.user)
        return queryset



class CreateIssue(LoginRequiredMixin, FormView):
    login_url = '/auth/login'
    model = Issue
    form_class = CreateIssueForm
    template_name = 'forms/on_site_issue.html'
    success_url = reverse_lazy('Core:Index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Issue'
        context['message'] = 'add'
        context['action_url'] = reverse_lazy('ONSite:CreateIssue')
        return context

    # create with save multiple file
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        issue = form.save(commit=False)
        file = request.FILES.getlist('file')

        if form.is_valid():
            issue = form.save(commit=False)
            issue.reporter = request.user
            issue.status = Status(1)
            issue.create = datetime.date.today()
            issue.save()
            if file != None:
                for f in file:
                    selected_files = f
                    Files.objects.create(files=selected_files, issue=issue, name=issue.title)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)



class IssueUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login'
    model = Issue
    form_class = CreateIssueForm
    template_name = 'forms/on_site_issue.html'
    success_url = reverse_lazy('Core:Index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'edit'
        context['info_obj'] = self.object
        context['action_url'] = reverse_lazy('ONSite:IssueUpdate', kwargs={'pk': self.object.id})
        return context

    def get_success_url(self):
        messages.success(self.request, "Edit Done Succesfuly", extra_tags="success")

        if self.request.POST.get('url'):
            return self.request.POST.get('url')
        else:
            return self.success_url


class FilesUpdate(LoginRequiredMixin, DetailView):
    login_url = '/auth/login/'
    model = Issue
    form_class = FilesForm
    template_name = 'files.html'
    success_url = reverse_lazy('Core:Index')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['files'] = Files.objects.filter(issue=self.object.id)
        context['action_url'] = reverse_lazy('ONSite:FilesUpdate', kwargs={'pk': self.object.id})
        return context

    def post(self, request, *args, **kwargs):
        file = request.FILES.getlist('file')
        issue = Issue.objects.get(id=kwargs['pk'])
        form = self.form_class()
        messages.success(self.request, "Files Done  ", extra_tags="success")

        if file != None:
            for f in file:
                selected_files = f
                obj=Files()
                obj.issue = issue
                obj.name = self.kwargs['pk']
                obj.files = selected_files
                obj.save()
        return HttpResponseRedirect(reverse_lazy('Core:Index'))


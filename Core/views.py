from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import  get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Issue, Status

# Create your views here.


@login_required(login_url='Auth:Login')
def Index(request):
    # open and clsoe user issue
    open_issue = Issue.objects.filter(reporter=request.user, status=Status(1))
    close_issue = Issue.objects.filter(reporter=request.user, status=Status(2))

    # all user issue
    issue = Issue.objects.filter(reporter=request.user).order_by('-id')

    # return count for open issue and close issue
    open_issue_count = open_issue.count()
    close_issue_count = close_issue.count()

    context = {
        'open_issue_count': open_issue_count,
        'close_issue_count': close_issue_count,
        'issue': issue
    }

    return render(request, 'core/index.html', context)



def index_div(request):
    open_issue = Issue.objects.filter(reporter=request.user, status=Status(1))
    close_issue = Issue.objects.filter(reporter=request.user, status=Status(2))

    issue = Issue.objects.filter(reporter=request.user).order_by('-id')

    open_issue_count = open_issue.count()
    close_issue_count = close_issue.count()
    context = {
        'open_issue_count': open_issue_count,
        'close_issue_count': close_issue_count,
        'issue': issue
    }
    return render(request, 'on_site_issue_div.html', context)


def IssueList(request, status):
    open_issue = Issue.objects.filter(reporter=request.user, status=Status(1))
    close_issue = Issue.objects.filter(reporter=request.user, status=Status(2))

    # open and close counter
    open_issue_count = open_issue.count()
    close_issue_count = close_issue.count()
    # issue for requested user and filtering by status nubmer
    issue = Issue.objects.filter(reporter=request.user, status=Status(status)).order_by('-id')
    context = {
        'issue': issue,
        'open_issue_count': open_issue_count,
        'close_issue_count': close_issue_count
    }
    return render(request, 'core/index.html', context)



def IssueList_div(request, status):
    open_issue = Issue.objects.filter(reporter=request.user, status=Status(1))
    close_issue = Issue.objects.filter(reporter=request.user, status=Status(2))

    # open and close counter
    open_issue_count = open_issue.count()
    close_issue_count = close_issue.count()
    # issue for requested user and filtering by status nubmer
    issue = Issue.objects.filter(reporter=request.user, status=Status(status)).order_by('-id')
    context = {
        'issue': issue,
        'open_issue_count': open_issue_count,
        'close_issue_count': close_issue_count
    }
    return render(request, 'on_site_issue_div.html', context)


 



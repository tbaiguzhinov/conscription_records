from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required

from regs.models import Personnel

@login_required
def home_view(request):

    employees = Personnel.objects.all()

    context = {'employees': employees}

    return render(request, 'home.html', context=context)


@login_required
def personnel_view(request, id):

    employee = get_object_or_404(Personnel, id=id)

    context = {'employee': employee}

    return render(request, 'card-template.html', context=context)


@login_required
def report_view(request):
    
    employees = Personnel.objects.all()

    context = {'employees': employees}

    return render(request, 'card_report.html', context=context)

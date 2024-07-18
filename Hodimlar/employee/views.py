# from django.http import HttpResponse

from django.shortcuts import render

from employee.models import Employee1


def home(req):
    hodimlar = Employee1.objects.all()

    context = {
        'hodimlar': hodimlar
    }

    return render(req, 'index.html', context)

def hodim(req, pk):
    hodim_ = Employee1.objects.get(pk=pk)

    context = {
        'hodim': hodim_
    }

    return render(req, 'hodim.html', context)

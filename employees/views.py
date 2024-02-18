from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Employee


# Create your views here.
def employee_detail(request, id):
    employee = get_object_or_404(Employee, pk=id)

    context = {
        "employee": employee,
    }
    return render(request, "employee_detail.html", context)
